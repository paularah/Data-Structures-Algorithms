package main

import (
	"errors"
)

const ArraySize int = 9

// type IhashTable interface {
// 	insert(key string)(error)
// 	remove(key string)(error)
// 	get(key string) (string, error)
// }

// type IlinkedList interface {
// 	insert(val string)
// 	remove(val string)
// 	search(val string)
// }


type hashTable struct {
	array [ArraySize]*bucket
}

type node struct {
	value string
	key string
	next  *node
}


type bucket struct {
	head *node
}

func (h *hashTable) get (key string) (string, error) {
	keyHash := hash(key, ArraySize)
	result, err := h.array[keyHash].get(key)
	return result, err
}

func (h *hashTable) insert (key string, value string) {
	keyHash := hash(key, ArraySize)
	h.array[keyHash].insert(key, value)
}

func (h *hashTable) remove (key string) (err error){
	keyHash := hash(key, ArraySize)
	h.array[keyHash].remove(key)
	return nil 
}


func InitHashTable() *hashTable {
	var result = &hashTable{}
	for i := range result.array {
		result.array[i] = &bucket{}
	}
	return result
}

func hash(key string, size int) int {
	sum := 0
	for _, v := range key {
		sum += int(v)
	}
	return sum % size
}


func (n *bucket) insert (key string, val string) {
	currentNode := n.head 
	for currentNode.next != nil {
		currentNode = currentNode.next
	}
	currentNode.next = &node{value: val, key:key}
}

func (n *bucket) remove (key string)  {
	currentNode := n.head
	var prevNode *node 

	for currentNode.key != key {
		prevNode = currentNode
		currentNode = currentNode.next
	}
	prevNode.next = currentNode.next

}

func (n *bucket) get(key string)(value string, err error) {
	currentNode := n.head 
	for currentNode.key != key && currentNode.next != nil {
		currentNode = currentNode.next
	}

	if currentNode.key != key {
		return "", errors.New("non existent value")
	}
	return currentNode.value, nil 

}


func main() {
	
}
