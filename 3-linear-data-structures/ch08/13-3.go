// Go
// 데크(deque) 자료형을 Go로 바닥부터 구현한 풀이
const minCapacity = 16

type Deque struct {
    buf    []interface{}
    head   int
    tail   int
    count  int
    minCap int
}

func (q *Deque) Len() int {
    return q.count
}

func (q *Deque) PushBack(elem interface{}) {
    q.growIfFull()

    q.buf[q.tail] = elem
    q.tail = q.next(q.tail)
    q.count++
}

func (q *Deque) PopFront() interface{} {
    if q.count <= 0 {
        panic("deque: PopFront() called on empty queue")
    }
    ret := q.buf[q.head]
    q.buf[q.head] = nil
    q.head = q.next(q.head)
    q.count--

    return ret
}

func (q *Deque) PopBack() interface{} {
    if q.count <= 0 {
        panic("deque: PopBack() called on empty queue")
    }

    q.tail = q.prev(q.tail)

    ret := q.buf[q.tail]
    q.buf[q.tail] = nil
    q.count--

    return ret
}

func (q *Deque) prev(i int) int {
    return (i - 1) & (len(q.buf) - 1)
}

func (q *Deque) next(i int) int {
    return (i + 1) & (len(q.buf) - 1)
}

func (q *Deque) growIfFull() {
    if len(q.buf) == 0 {
        if q.minCap == 0 {
            q.minCap = minCapacity
        }
        q.buf = make([]interface{}, q.minCap)
        return
    }
    if q.count == len(q.buf) {
        q.resize()
    }
}

func (q *Deque) resize() {
    newBuf := make([]interface{}, q.count<<1)
    if q.tail > q.head {
        copy(newBuf, q.buf[q.head:q.tail])
    } else {
        n := copy(newBuf, q.buf[q.head:])
        copy(newBuf[n:], q.buf[:q.tail])
    }

    q.head = 0
    q.tail = q.count
    q.buf = newBuf
}

func isPalindrome(head *ListNode) bool {
    var q Deque

    if head == nil {
        return true
    }
    node := head
    for node != nil {
        q.PushBack(node.Val)
        node = node.Next
    }

    for q.Len() > 1 {
        if q.PopFront() != q.PopBack() {
            return false
        }
    }

    return true
}