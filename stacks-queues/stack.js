/*
 The stack abstarct data type implementation using linked list.
 This is achieved by using the popFirst and prepend primary methods of
 a linked list. Having a reference to the tail is this case is redundant, since all primary
 methods can be achieved by leveraging on the head node.
 */

//  A ndoe Class
 class Node{
     constructor(val){
        //  the node class has value and the next as it attributes
         this.val = val;
         this.next = null;
     }
 }


//Stack Class
 class Stack{
     constructor(){
        //  equivalent to the head of a linked list
        this.first = null;
        // the length of the stack
        this.size = 0;

     }

    //  push method
     push(val){
        //  make a new node that references the value
         let newNode = new Node(val);
        //  set the next property of the newNode to the first node
         newNode.next = this.first
        //  Make the new node the first node
         this.first = newNode;
        //  Increement and return the length
         return ++this.size;
     }

    //  pop method
     pop(){
        // dealing with the egde case of an empty stack
        // return null ? !this.first:{}
        if (!this.first){
            return null;
        }
         let newFirst = this.first.next;
        //  severe the link between the head and the rest of nodes
        this.first.next = null;
        // save of value in the first node
        let value = this.first.val;
        // make the second node the first node
        this.first = newFirst;
        // decrement the length
        this.size--;
        // and return the value of the previous first node
        return value;
     }

    //  peek method
     peek(){
         // dealing with the egde case of an empty stack
        if (!this.first){
            return null;
        }

        return this.first.val;

     }
 }


//  Unit tests
const test = () =>{
    const assert = require('assert')
    // requiring the node in-built module assertaion testing for unit
    // test
    const myStack = new Stack();
    myStack.push(4);
    let actual = myStack.first.val;
    assert.deepStrictEqual(actual, 4);
    // testing LIFO
    myStack.push(2);
    actual = myStack.first.val;
    assert.deepStrictEqual(actual, 2);
    myStack.push(0);
    actual = myStack.first.val
    assert.deepStrictEqual(actual, 0);
    actual = myStack.first.next.next.val
    assert.deepStrictEqual(actual, 4);
    // testing pop method
    actual = myStack.pop();
    assert.deepStrictEqual(actual, 0);
    // testing peek method
    actual = myStack.peek();
    assert.deepStrictEqual(actual, 2);
    // testing a edge case
    myStack.pop();
    myStack.pop();
    actual = myStack.peek();
    assert.deepStrictEqual(actual, null);
    actual = myStack.pop();
    assert.deepStrictEqual(actual, null);
}

test();
