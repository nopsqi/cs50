import Matter from "matter-js";
import game from "./src/resources/game";
import ball from "./src/resources/entities/ball";
import plank from "./src/resources/entities/plank";
import welcome from "./src/resources/pages/welcome";
import "./style.css";

Matter.Events.on(game.engine, "collisionActive", (e) => {
    let plankCollision;
    for (let i = 0; i < e.pairs.length; i++) {
        if (e.pairs[i].bodyA === plank.body || e.pairs[i].bodyB === plank.body) {
            plankCollision = e.pairs[i];
            continue;
        }

        if (e.pairs[i].collision.depth > ball.body.circleRadius * 2) {
            if (plankCollision) {
                plankCollision.isActive = false;
                plankCollision.isSensor = true;
                break;
            }
        }
    }
});

Matter.Events.on(game.engine, "collisionEnd", (e) => {
    for (let i = 0; i < e.pairs.length; i++) {
        if (e.pairs[i].bodyA === plank.body || e.pairs[i].bodyB === plank.body) {
            continue;
        }
        ball.body.isSensor = false;
        plank.body.isSensor = false;
        break;
    }
});
ball.onfalling((entity) => {
    ball.reset();
    plank.reset();
});
game.addEntity([ball, plank]);
game.addPage(welcome);

game.update(() => {
    ball.update();
});
