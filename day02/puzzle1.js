function* range(n) {
    i = 0;
    while (true) {
        while (i < n)
            yield i++;
        break
    }
    return i
}

let r = range(4)
for (let i of r) {
    console.log(i)
}

let sequence = [...range(5)]
console.log(sequence)
