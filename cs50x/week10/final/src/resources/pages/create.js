import * as PIXI from "pixi.js";
import Matter from "matter-js";
import TextInput from "pixi-text-input";
import game from "../game";
import Button from "../../classes/Button";
import Page from "../../classes/Page";
import Hole from "../../classes/Hole";
import welcome from "./welcome";
import levels from "../levels";

const buttons = [
    {
        text: "Clear",
        position: {
            x: 20 + 50,
            y: 20 + 30,
        },
        eventsHandler: {
            onpointerdown: (e) => {
                e.target.page.onclear();
            },
        },
    },
    {
        text: "Save",
        position: {
            x: 600 - 150 - 40,
            y: 30 + 20,
        },
        eventsHandler: {
            onpointerdown: (e) => {
                e.target.page.onsave();
            },
        },
    },
    {
        text: "Back",
        position: {
            x: 600 - 50 - 20,
            y: 50,
        },
        eventsHandler: {
            onpointerdown: (e) => {
                e.target.onpointerleave(e);
                e.target.page.onback();
            },
        },
    },
];

const create = new Page();
const savePopUp = new PIXI.Container();
savePopUp.visible = false;
savePopUp.position.set(300, 500);
const savePopUpButtons = [
    {
        text: "Submit",
        position: {
            x: -70,
            y: 30 + 25,
        },
        eventsHandler: {
            onpointerdown: (e) => {
                e.target.onpointerleave(e);
                e.target.page.onsubmit();
            },
        },
    },
    {
        text: "Cancel",
        position: {
            x: 70,
            y: 30 + 25,
        },
        eventsHandler: {
            onpointerdown: (e) => {
                e.target.onpointerleave(e);
                e.target.page.oncancel();
            },
        },
    },
];
savePopUpButtons.forEach((options) => {
    const button = new Button(
        options.text,
        options.position,
        options.eventsHandler
    );
    button.page = create;
    savePopUp.addChild(button);
});
const input = new TextInput({
    input: {
        fontSize: "36px",
        padding: "12px",
        width: "300px",
        color: "#26272E",
    },
    box: {
        default: {
            fill: 0xe8e9f3,
            rounded: 12,
            stroke: { color: 0xcbcee0, width: 3 },
        },
        focused: {
            fill: 0xe1e3ee,
            rounded: 12,
            stroke: { color: 0xabafc6, width: 3 },
        },
        disabled: { fill: 0xdbdbdb, rounded: 12 },
    },
});
input.position.set(-(input.width / 2) + 10, -input.height - 25);
savePopUp.addChild(input);
create.container.addChild(savePopUp);
const interfaceContainer = new PIXI.Container();
buttons.forEach((options) => {
    const button = new Button(
        options.text,
        options.position,
        options.eventsHandler
    );
    button.page = create;
    interfaceContainer.addChild(button);
});
create.container.addChild(interfaceContainer);

const mouse = Matter.Mouse.create(game.app.view);
const mouseConstraint = Matter.MouseConstraint.create(game.engine, {
    mouse: mouse,
    constraint: {
        stiffness: 0.2,
        render: {
            visible: false,
        },
    },
});
create.container.eventMode = "static";
create.container.hitArea = game.app.screen;
const holeContainer = new PIXI.Container();
holeContainer.name = "holeContainer";
let dragTarget = null;
create.container.onpointerdown = (containerEvent) => {
    if (containerEvent.target !== create.container) {
        return;
    }
    Matter.Events.on(mouseConstraint, "mousedown", (mouseConstraintEvent) => {
        if (!mouseConstraintEvent.source.body) {
            const hole = new Hole(
                mouseConstraintEvent.mouse.position.x,
                mouseConstraintEvent.mouse.position.y
            );
            Matter.Composite.add(create.composite, hole.body);
            hole.graphics.eventMode = "static";
            hole.graphics.cursor = "pointer";
            hole.graphics.onpointerdown = (graphicsEvent) => {
                dragTarget = graphicsEvent.target;
                create.container.onpointermove = (containerEvent) => {
                    if (dragTarget) {
                        dragTarget.position.set(
                            hole.body.position.x,
                            hole.body.position.y
                        );
                    }
                };
            };

            holeContainer.addChild(hole.graphics);
        }
    });
};
create.container.addChildAt(holeContainer, 0);

create.container.onpointerup = () => {
    if (mouseConstraint.events.mousedown) {
        Matter.Events.off(mouseConstraint, "mousedown");
    }
    dragTarget = null;
    create.container.onpointermove = null;
};

Matter.Events.on(mouseConstraint, "startdrag", (mouseConstraintEvent) => {
    if (mouseConstraintEvent.body.label == "hole") {
        Matter.Body.setStatic(mouseConstraintEvent.body, false);
    }
});

Matter.Events.on(mouseConstraint, "enddrag", (e) => {
    if (e.body.label == "hole") {
        Matter.Body.setStatic(e.body, true);
    }
    create.container.onpointermove = null;
});

Matter.Composite.add(create.composite, mouseConstraint);

create.onback = () => {
    game.switchPage(create, welcome);
};
create.onsave = () => {
    savePopUp.visible = true;
};
create.onclear = () => {
    Matter.Composite.remove(create.composite, create.composite.bodies);
    holeContainer.removeChildren();
};
create.onsubmit = () => {
    levels.add({
        name: input.text,
        holes: create.composite.bodies.map((body) => body.position),
    });
    create.oncancel();
    create.onclear();
};
create.oncancel = () => {
    savePopUp.visible = false;
};

export default create;
