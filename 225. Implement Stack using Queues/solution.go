type MyStack struct {
    queue []int
}


/** Initialize your data structure here. */
func Constructor() MyStack {
    return MyStack{}
}


/** Push element x onto stack. */
func (this *MyStack) Push(x int)  {
    this.queue = append(this.queue, x)
}


/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
    l := len(this.queue)
    for i:=0; i<l-1; i++ {
        x := this.queue[0]
        this.queue = this.queue[1:]
        this.queue = append(this.queue, x)
    }
    x := this.queue[0]
    this.queue = this.queue[1:]
    return x
}


/** Get the top element. */
func (this *MyStack) Top() int {
    return this.queue[len(this.queue)-1]
}


/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
    if len(this.queue) == 0 {
        return true
    } else {
        return false
    }
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
