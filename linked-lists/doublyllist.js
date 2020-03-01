
// The node class 
class Node{
    constructor(val){
        this.val = val;
        this.next = null;
        this.pre = null;
    }
}

// The doubly linked list class
class doublyLinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    // append method
    append(val){
        let newNode = new Node(val);
        if (!this.head){
            this.head =  newNode;
            this.tail = newNode;
        }else{
            this.tail.next = newNode;
            newNode.pre = this.tail;
            this.tail  = newNode;
            this.size++;
        }  
    }

    prepend(val){
        let newNode = new Node(val);
        if (!this.head){
            this.head = newNode;
            this.tail = newNode;
        }else{
            let hold = this.head;
            newNode.next = this.head;
            this.head.pre = newNode;
            this.head = newNode;
            this.size++;
        }

     
    }

    popFirst(){
        if (!this.head || !this.tail) return undefined;
        let currentHead = this.head;
        let newHead = this.head.next;
        currentHead.next = null;
        newHead.pre = null;
        this.head = newHead;
        this.size--;
        return currentHead.val;
    }

    popLast(){
        if (!this.tail || !this.tail) return undefined;
        let currentTail = this.tail;
        let newTail = this.tail.pre;
        currentTail.pre = null;
        newTail.next = null;
        this.tail = newTail;
        return currentTail.val;
    }

    // switched back to 0 based indexing based on the problems ecountered 
    // with one based indedxing in the sinlylinked list 
    insert(index, val){
        // handling the edge case of an index smaller than 0
        if (index < 0) return undefined;
        // simply prepending if the index is 0
        if (index === 0) return this.prepend(val);
        // simply appending if the index is the size
        if (index === this.size) return this.append(val);
        // getting the previous node befoore the postion we want to
        // insert in
        index = index -1;
        let count, current;
        // transversing either from the head or tail depending the closeness of 
        // of the index
        if(index <= this.length/2){
            count = 0;
            current = this.head;
            while(count !== index){
                current = current.next;
                count++;
            }
        } else {
            count = this.length - 1;
            current = this.tail;
            while(count !== index){
                current = current.prev;
                count--;
            }
        }

        // chaining the nodes together

        let newNode = new Node(val);
        let NextNode = current.next;
        current.next = newNode;
        newNode.pre = current;
        newNode.next = NextNode;
        NextNode.pre = newNode;
        this.size++;
    }

    delete(index){
        // handling edge cases 
        if(index < 0 || index >= this.size) return undefined;
        if(index === 0) return this.popFirst();
        if(index === this.size - 1) return this.popLast();
        // tranversing to the index to be deleted
        let count, current;
        // transversing either from the head or tail depending the closeness of 
        // of the index
        if(index <= this.length/2){
            count = 0;
            current = this.head;
            while(count !== index){
                current = current.next;
                count++;
            }
        } else {
            count = this.length - 1;
            current = this.tail;
            while(count !== index){
                current = current.prev;
                count--;
            }
        }
        current.pre.next = current.next;
        current.next.pre = current.pre;
        current.next = null;
        current.pre = null;
        this.size--;


    }

}


const test = ()=>{
    const assert = require('assert');
    const list = new doublyLinkedList();
    // testing the append method of our linked list
    list.append(5);
    // testig the previous property 
    assert.deepStrictEqual(list.head.pre, null);
    list.append(6);
    // testing the head property of the linked dlist
    assert.deepStrictEqual(list.head.val, 5);
    // testing the next property
    assert.deepStrictEqual(list.head.next.val, 6);
    // testing the prepend method 
    list.prepend(1);
    assert.deepStrictEqual(list.head.val, 1);
    // testing the pop first method
    let first  = list.popFirst();
    assert.deepStrictEqual(first, 1);
    // testing the pop last method
    let last = list.popLast();
    assert.deepStrictEqual(last, 6)
    // testing the insert method
    list.insert(0, 9);
    assert.deepStrictEqual(list.head.val, 9)
    // testing the delete method
    list.delete(1);
}

test();
