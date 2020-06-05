fin = open('mixmilk.in')
buckets = []
buckets_size = []
for line in fin:
    line = line.strip()
    size, init = line.split(' ')
    buckets.append(init)
    buckets_size.append(size)
fin.close()
class Bucket:
    def __init__(self, bucket_init, bucket_size):
        self.initial = int(bucket_init)
        self.size = int(bucket_size)
    def combine(self, other):
        if self.initial + other.initial > other.size:
            self.initial = self.initial + other.initial - other.size
            other.initial = other.size
        else :
            other.initial = self.initial + other.initial
            self.initial = 0
Bucket1=Bucket(buckets[0], buckets_size[0])
Bucket2=Bucket(buckets[1], buckets_size[1])
Bucket3=Bucket(buckets[2], buckets_size[2])
for i in range(33):
    Bucket1.combine(Bucket2)
    Bucket2.combine(Bucket3)
    Bucket3.combine(Bucket1)
Bucket1.combine(Bucket2)
fout = open("mixmilk.out", "w")
fout.write("{}\n".format(Bucket1.initial))
fout.write("{}\n".format(Bucket2.initial))
fout.write("{}".format(Bucket3.initial))
fout.close()
