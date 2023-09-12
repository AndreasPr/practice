if __name__ == "__main__":

    L, N, k, Q = map(int, input().split())

    input_string = ""
    for _ in range(L):
        input_string += input().strip()        

    kmer_count = {}
    for i in range(N - k + 1):
        kmer = input_string[i:i + k]
        kmer_count[kmer] = kmer_count.get(kmer, 0) + 1
        

    for _ in range(Q):
        kmer = input().strip()
        print(kmer, kmer_count.get(kmer, 0))
