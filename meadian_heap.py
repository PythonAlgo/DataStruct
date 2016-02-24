from __future__ import division
import max_heap as maxh
import min_heap as minh

def main():
    count = int(input())
    max_heap = maxh.MaxHeap()
    min_heap = minh.MinHeap()

    # put first element in one of the heap
    first = int(input())
    second = int(input())

    if first > second:
        max_heap.insert(second)
        min_heap.insert(first)
    else:
        max_heap.insert(first)
        min_heap.insert(second)


    # set the first median
    print first
    median = (first + second)/ 2
    print median
    for i in range(1, count-1):
        this_num = int(input())
        if this_num < max_heap.peek_max():
            max_heap.insert(this_num)
        else:
            min_heap.insert(this_num)
        balance_heaps(max_heap, min_heap)
        print(get_median(max_heap, min_heap))


def get_median(max_heap, min_heap):
    if max_heap.size > min_heap.size:
        return max_heap.peek_max()
    elif min_heap.size > max_heap.size:
        return min_heap.peek_min()
    else:
        return (max_heap.peek_max() + min_heap.peek_min())/2


def balance_heaps(max_heap, min_heap):
    """
    balances the heaps if the size are mispatched
    :param max_heap:
    :param min_heap:
    :return: none
    """
    if abs(max_heap.size - min_heap.size) <= 1:
        return
    else:
        # move root from more size to lower
        if max_heap.size > min_heap.size:
            root = max_heap.get_max()
            min_heap.insert(root)
        else:
            root = min_heap.get_min()
            max_heap.insert(root)

        # call balance heap again
        balance_heaps(max_heap, min_heap)



if __name__ == "__main__":
    main()