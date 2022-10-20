package main

type IhashTable interface {
	insert(key string)
	remove(key string)
	get(key string) string
}

type IlinkedList interface {
	insert(val string)
	remove(val string)
	search(val string)
}

func InitHashTable(size int) *IhashTable {
	var array [size]*bucket
}

func hash(key string, size int) int {
	sum := 0
	for _, v := range key {
		sum += int(v)
	}
	return sum % size
}


type hashTable struct {
	array []*Bucket
}

type bucket struct {
	head *node
}

func insert(node *bucket) (val string) {
	temp := node.head 
	for temp.next != nil {
		temp = temp.next
	}

	temp.next = &node{val}
}

func remove(node *bucket) (val string) {
	temp := node.head
	prev := nil 
	for temp
}



type node struct {
	value string
	next  *bucket
}

func main() {

}
