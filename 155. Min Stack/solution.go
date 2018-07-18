type MinStack struct {
    stack []int
    min []int
}


/** initialize your data structure here. */
func Constructor() MinStack {
    return MinStack{}
}


func (this *MinStack) Push(x int)  {
    if len(this.stack) != 0 {
        l := len(this.min)-1
        if this.min[l] > x {
            this.min = append(this.min, x)
        } else {
            this.min = append(this.min, this.min[l])
        }
    } else {
        this.min = append(this.min, x)
    }
    this.stack = append(this.stack, x)
}


func (this *MinStack) Pop()  {
    l := len(this.stack) - 1
    if l >= 0 {
        this.stack = this.stack[:l]
        this.min = this.min[:l]
    }
}


func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1]
}


func (this *MinStack) GetMin() int {
    return this.min[len(this.min)-1]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
