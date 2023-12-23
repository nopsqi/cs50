import Matter from "matter-js";
import * as PIXI from "pixi.js";
import Page from "./Page";

export default class Game extends Page {
    constructor() {
        const engine = Matter.Engine.create({
            gravity: { x: 0, y: 9, scale: 0.001 },
        });
        const app = new PIXI.Application({
            width: 600,
            height: 1000,
            background: "#111",
            antialias: false,
        });
        globalThis.__PIXI_APP__ = app;
        document.body.appendChild(app.view);

        super(engine.world, app.stage);
        this._life = 3;
        this.engine = engine;
        this.app = app;
    }
    get life() {
        return this._life;
    }
    set life(value) {
        if (value < 0) {
            throw "ZeroLife";
        }
        this._life = value;
    }
    addPage = (pages) => {
        [].concat(pages).forEach((page) => {
            Matter.Composite.add(this.composite, page.composite);
            this.container.addChild(page.container);
        });
    };
    removePage = (pages) => {
        [].concat(pages).forEach((page) => {
            Matter.Composite.remove(this.composite, page.composite);
            this.container.removeChild(page.container);
        });
    };
    switchPage = (page, otherPage) => {
        this.removePage(page);
        this.addPage(otherPage);
    };
    update = (callback) => {
        this.app.ticker.add(() => {
            Matter.Engine.update(this.engine, 1000 / 60);
            callback();
        });
    };
}
