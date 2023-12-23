import Matter from "matter-js";
import * as PIXI from "pixi.js";

export default class Entity {
    constructor(body, graphics) {
        this.body = body;
        this.graphics = graphics;
    }
}
