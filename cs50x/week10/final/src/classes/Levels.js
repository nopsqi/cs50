import Level from "./Level";

export default class Levels {
    constructor(json) {
        this._index = 0;
        this.children = []
            .concat(json)
            .map((level) => new Level(level.name, level.holes));
    }
    get current() {
        return this.children[this._index];
    }
    get first() {
        return this.children[0];
    }
    get last() {
        return this.children[this.children.length - 1];
    }
    reset() {
        this._index = 0;
    }
    next() {
        if (this._index + 1 > this.children.length - 1) {
            throw "MaxReached";
        }
        this._index += 1;
    }
    previous() {
        if (this._index - 1 < 0) {
            throw "MinReached";
        }
        this._index -= 1;
    }
    add(data) {
        this.children.push(new Level(data.name,  data.holes))
    }
}
