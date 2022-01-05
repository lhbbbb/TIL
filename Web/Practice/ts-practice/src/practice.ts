const msg: string = 'hello world'
console.log(msg)

interface Person {
    name: string;
    age: number;
}

const person: Person = {
    name: 'h',
    age: 20
}

function merge<T>(a: T) {
    a
}

const merged = merge({ foo: 1, bar: '' })