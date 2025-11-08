function createCounter(n: number): () => number {
    let base = n
    return function() {
        return base++
    }
}


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */