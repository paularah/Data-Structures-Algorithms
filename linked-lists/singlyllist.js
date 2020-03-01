// Node class with reference to the next node and the value 
class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

// Linked list class with reference to the first, tail and the size
class SinglyLinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    // a listthod for appending to the end 
    append(val){
        // creating a new node reference to the value to be appended 
        let newNode = new Node(val);
        // handling edge case of an empty list
        if (!this.head){
            this.head = newNode;
            this.tail = newNode;
        }
        this.tail.next = newNode;
        this.tail = newNode
        this.size++;
    }

    // method for transversing through a list
    transverse(){
        let current = this.head;
        while (current){
            console.log(current.val);
            current = current.next;
        }
    }

    // removes the last node and returns it value
    popLast(){
        if (!this.head) return undefined;
        let current = this.head;
        let newTail = current;
        while(current.next){
            newTail = current;
            current = current.next;
        }
        this.tail = newTail;
        newTail.next = null;
        if (this.size === 1){
            this.head = null;
            this.tail = null;
        }
        this.size--;
        return current.val; 

    }

    // removes the first node and return its value
    popFirst(){
        if (!this.head){
            return null;
        }
        let currentHead = this.head;
        let newHead = this.head.next;
        currentHead.next = null;
        this.head = newHead;
        this.size--;
        return currentHead.val;
    }

    // adding A node to the begining of a list
    prepend(val){
        let newHead = new Node(val);
        // hadling the edge case fof an empty list
        if(!this.head){
            this.head = newHead;
            this.tail = newHead;
        }
        newHead.next = this.head;
        this.head = newHead;
        this.size++;
        return this;
    }

    // 1 based indexing
    get(index){
        if (index > this.size || index < 1){
            return undefined;
        } 
        let current = this.head;
        for(let i = 1; i < index; i++){
            current = current.next;
        }
        return current.val;
    }

    // inserting a node at given index
    insert(index, val){
        //this is beacause we using one based indexing
        if (index < 1 || index > this.size+1) return undefined;
        let newNode =  new Node(val);
        // Handling the egde case of insert into an empty singly
        // this arises as a result of using one based indexing.
        if (this.size === 0){
            this.append(newNode)
            return this.head.val;
        }
        // transversing through the nodes
        let current = this.head;
        for (let i = 1; i < index; i++){
            current = current.next;
        }
        let nextNode = current.next;
        current.next = newNode;
        newNode.next = nextNode;
    }
}



// unit test 
const test = () =>{
    // node in bulit module assertion testing for unit test
    const assert = require('assert');
    // new instance of the singlylinkedlist class
    let list = new SinglyLinkedList;
    list.append(2); list.append(0); list.append(1);
    // testing the append primary method
    assert.deepStrictEqual(list.head.val, 2);
    // testing the popfirst method
    list.popFirst();
    assert.deepStrictEqual(list.head.val, 0);
    // testing the prepend method
    list.prepend(7);
    assert.deepStrictEqual(list.head.val, 7);
    // testing the tail property 
    assert.deepStrictEqual(list.tail.val, 1);
}

test();
