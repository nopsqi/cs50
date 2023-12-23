import Matter from "matter-js";
import * as PIXI from "pixi.js";
import Hole from "./Hole";

export default class Level {
    constructor(name, holes) {
        this.name = name;
        this.holes = holes.map((hole) => new Hole(hole.x, hole.y, 40));
        this.composite = Matter.Composite.create();
        this.holes.forEach((hole) => Matter.Composite.add(this.composite, hole.body));
        this.container = new PIXI.Container();
        this.holes.forEach((hole) => this.container.addChild(hole.graphics));
    }
}
