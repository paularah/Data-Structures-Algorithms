/*
Implementation of the queue abstract data type. This is also achived leveraging
on the primary methods of linked list.
 */

//  The node class
 class Node{
    //  has val and reference to the next as it attributes
     constructor(val){
         this.val = val;
         this.next = null;
     }
 }

//  Queue class
 class Queue{
    //  The queue ADT class with first, last and length as it attributes
     constructor(){
         this.first = null;
         this.last = null;
         this.size = 0;
     }

    //  The enqueue method
     enque(val){
        //  creating a new node with refrence to the value to be enqueued
        let newNode = new Node(val);
        // edge case to handle an empty queue
         if (!this.first){
             this.first = newNode;
             this.last = this.first;
         }
        // assingning the next property of the last node to the new queue
         this.last.next = newNode;
        //  making the new queue the last node
         this.last = newNode
        //  Incrementing the length
         this.size ++;
     }

    //  dequeue method
     dequeue(){
        //  Handling the egde case of an empty queue
         if (!this.first){
             return null;
         }
        // getting and storing the value on the first node
         let value = this.first.val;
        //  getting the next property of the first node
         let newFirst = this.first.next;
        //  severing the link between the first node and other node
        // and making the newFirst node the first node.
         this.first = newFirst;
        // Decrementing the length
         this.size --;
        //  returning the value of the previous frist first node
         return value;
     }

    //  peek method
     peek(){
        //  Handling the edge case of an empty queue
         if(!this.first){
             return null;
         }
        //  returnign the value of the first node
         return this.first.val;
     }
 }



//  unit test
 const test = () => {
     // requiring the node in-built module assertaion testing for unit
    // test
    const assert = require('assert');
    // new objet of our queue
    myQueue = new Queue();
    let actual = myQueue.first();
    // testing te egde case of an empty node
    assert.deepStrictEqual(actual, null);
    // testing size
    assert.deepStrictEqual(myQueue.size, 0)
    // testing enque method
    myQueue.enque(1);
    actual = myQueue.first.val
    // testing size increment
    assert.deepStrictEqual(actual, 1);
    myQueue.enque(3);
    assert.deepStrictEqual(myQueue.size, 2);
    assert.deepStrictEqual(myQueue.last.val, 3);
    // testing deque method
    actual = myQueue.dequeue();
    assert.deepStrictEqual(actual, 1)
    assert.deepStrictEqual(myQueue.peek(), 1)

 }

 test();
