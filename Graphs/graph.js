class Grpah{
    constructor(){
        this.adjacencyList = {}
    }

    addVertex(vertex){
        if(!this.adjacencyList[vertex])this.adjacencyList[vertex] = []
    }
}