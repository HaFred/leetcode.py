from scipy.cluster.vq import kmeans  # just for code jump and look up the implementation wrapped inside
import collections

def kmeans(k: int, pts):  # pts 2d arr, [n, 2]
    centroids = []

    def cal_dist(point, centroid):
        dx = point[0] - centroid[0]
        dy = point[1] - centroid[1]
        return dx**2+dy**2

    # init centroid
    for i in range(k):
        centroids.append(pts[i])
        # centroids.append([random.randint(0, 300), random.randint(0, 300)])

    # init each pts label
    pts_label = [0 for i in range(len(pts))]  # [n, 1]
    label_cluster = collections.defaultdict(list)  # each key-val store the pts with the same label
    collections.OrderedDict
    for t in range(100):  # do 100 iterations
        # find each pt label
        for pidx in range(len(pts)):
            pt_min_dist_across_centroids = float('inf')
            closet_label = -1  # important to set it as none label, otherwise
            for label, ctd in enumerate(centroids):
                new_dist = cal_dist(pts[pidx], ctd)
                if pt_min_dist_across_centroids > new_dist:
                    pt_min_dist_across_centroids = new_dist
                    closet_label = label
            label_cluster[closet_label].append(pidx)  # to do append with the null dict, this dict needs to be instantiated as `defaultdict` with the default_factory as List
            pts_label[pidx] = closet_label

        # update each centroid position
        for label in label_cluster:
            new_centroid_x = sum([pts[p][0] for p in label_cluster[label]]) / len(label_cluster[label])
            new_centroid_y = sum([pts[p][1] for p in label_cluster[label]]) / len(label_cluster[label])
            centroids[label] = [new_centroid_x, new_centroid_y]

    return pts_label

# for vis: https://blog.csdn.net/weixin_45690272/article/details/105748829

def kmeans_chinese(k, positions):
    def getDistance(pos1, pos2):
        # x1,y1,x2,y2二维数组——就是平方距离即可，也不必开根号了
        return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2

    def getNewCenter(posList):
        centerX, centerY = 0, 0
        for pos in posList:  # 取这个中心所有点的距离平均值！！作为最后更新的质心，绝了
            centerX += pos[0]
            centerY += pos[1]

        return (centerX / len(posList), centerY / len(posList))


    class_center = positions[:k]  # 初始化默认自己就是自己中心
    sample_class = [None for i in range(len(positions))]  # 聚类结果
    iteration = 0

    while iteration < 100:  # 迭代T次
        # 记录k个类别的簇，编号呗
        class_cluster = collections.defaultdict(list)  # 字典，收集key-value，value就是类别key的归类类别
        for i in range(len(positions)):  # N个点
            cur = positions[i]  # 取出这个点xy
            min_distance = float('inf')  # max
            trulabel = -1  # 目前默认没有类别
            for label in range(k):  # k个簇
                # 计算cur跟所有k个簇质心的距离——把前面k个点，作为标准的聚类中心
                center = class_center[label]
                distance = getDistance(cur, center)  # 计算cur跟原类别质心的距离
                if distance < min_distance:
                    min_distance = distance
                    trulabel = label  # 新来的一个距离不错，就将其归类到这里
            # 最后一个OK的结果，放for外面哦
            class_cluster[trulabel].append(cur)  # 每个簇类别记录了cur属于自己——记录的就是一个一个点的xy坐标
            sample_class[i] = trulabel  # 这一轮迭代的结果——取最小这个簇囊括i这个点

        # 更新几个簇的质心
        for label in class_cluster:  # 每个类别里面都放了哪些下标
            new_center = getNewCenter(class_cluster[label])
            class_center[label] = new_center  # 换中心了
        iteration += 1

    return sample_class  # 最后一次的结果，就是最终的聚类结果


if __name__ == '__main__':
    arr = [
        [1.5, 2.1],
        [0.8, 2.1],
        [1.3, 2.1],
        [110.5, 260.6],
        [21.7, 32.8],
        [130.9, 150.8],
        [32.6, 40.7],
        [41.5, 24.7]
    ]
    k = 3
    # expects: [1, 1, 1, 0, 2, 0, 2, 2]
    print(kmeans(k, arr))
    # print(kmeans_chinese(k, arr))
