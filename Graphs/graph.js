class Grpah {
    constructor() {
        this.adjacencyList = {}
    }

    addVertex(vertex) {
        if (!this.adjacencyList[vertex]) this.adjacencyList[vertex] = []
    }

    addEdge(vertex1, vertex2) {
        this.adjacencyList[vertex1].push(vertex2)
        this.adjacencyList[vertex2].push(vertex1)
    }

    removeEdge(vertex1, vertex2) {
        this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter((vertex) => {
            return vertex != vertex2
        })
        this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter((vertex) => {
            return vertex != vertex1
        })

    }

    removeVertex(vertex){
        while(this.adjacencyList[vertex].length){
            const adjacentVertex = this.adjacencyList[vertex].pop()
            this.removeEdge(vertex, adjacentVertex)
        }
        delete this.adjacencyList[vertex]
    }

    DFS(start){
        result = []
        visited = {}
        let adjacencyList = this.adjacencyList

        function dfsRecur(vertex){
            if (!vertex) return null 
            visited[vertex] =  true
            result.push(vertex) 
            adjacencyList.forEach((neigbor) => {
                if (!visited[neigbor]){
                    return dfsRecur(neigbor)
                    
                }
            })
        } 

        dfsRecur(start)
        return result
    }

    DFS_I(start) {
        let stack = [start]
        let result = []
        let visited = {}
        let currentVertex;

        visited[start] = true 

        while (stack.length){
            currentVertex =  stack.pop()
            this.adjacencyList[currentVertex].forEach(neigbor => {
                if !visited[neigbor]
            })
        }

    }
}


