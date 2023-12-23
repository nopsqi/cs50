import Matter from "matter-js";
import * as PIXI from "pixi.js";

export default class Page {
    constructor(composite, container) {
        this.composite = composite || Matter.Composite.create();
        this.container = container || new PIXI.Container();
    }
    addContainer = (container) => {
        container.children.forEach((child) => (child.page = this));
        this.container.addChild(container);
    };
    addContainerAt = (container) => {
        container.children.forEach((child) => (child.page = this));
        this.container.addChildAt(container, 0);
    }
    removeContainer = (container) => {
        this.container.removeChild(container);
    };
    addComposite = (composite) => {
        composite.bodies.forEach((body) => (body.page = this));
        Matter.Composite.add(this.composite, composite);
    };
    removeComposite = (composite) => {
        Matter.Composite.remove(this.composite, composite);
    };
    addEntity = (entities) => {
        [].concat(entities).forEach((entity) => {
            this.container.addChild(entity.graphics);
            Matter.Composite.add(this.composite, entity.body);
        });
    };
}
