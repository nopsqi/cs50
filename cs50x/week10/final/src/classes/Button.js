import * as PIXI from "pixi.js";

export default class Button extends PIXI.Graphics {
    constructor(text, position, eventsHandler) {
        super();
        this.beginFill(0xffffff).drawRect(-50, -30, 100, 60).endFill();
        const textContainer = new PIXI.Text(text);
        textContainer.anchor.set(0.5);

        this.addChild(textContainer);
        this.position.set(position.x, position.y);
        this.eventMode = "static";
        this.cursor = "pointer";
        Object.entries(eventsHandler || {}).forEach((eventHandler) => {
            this[eventHandler[0]] = eventHandler[1];
        });
    }
    onpointerenter = (e) => (e.target.tint = 0x9f9f9f);
    onpointerleave = (e) => (e.target.tint = 0xffffff);
}
