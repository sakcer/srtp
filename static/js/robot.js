import * as THREE from "https://unpkg.com/three@0.138.0/build/three.module.js"
// import { OrbitControls } from 'OrbitControls';
// import { GLTFLoader } from 'GLTFLoader';

const g_color = 0xddddda;
let g_robot = {
    head: {
        r: 10,
    },
    body: {
        r: 10,
        h: 20,
    },
    shoulder: {
        r: 5,
    },
    arm: {
        r: 3,
        h: 15,
    },
    hand: {
        r: 4,
    },
    leg: {
        r: 3.5,
        h: 18,
    },
    foot: {
        r: 5,
    }

};

function Ball(r, ws, hs) {
    const geometry = new THREE.SphereGeometry(r, ws, hs);
    return geometry;
}

function Box(w, h, d) {
    const geometry = new THREE.BoxBufferGeometry(w, h, d);
    return geometry;
}

function HalfBall(r, ws, hs) {
    var geometry = new THREE.SphereGeometry(r, ws, hs, 0, Math.PI * 2, 0, Math.PI / 2);
    return geometry;

}

function Cylinder(rt, rb, h, rs, hs) {
    var geometry = new THREE.CylinderGeometry(rt, rb, h, rs, hs, false);
    return geometry;
}

function createMaterial(m) {
    // return new THREE.MeshPhongMaterial(m); // simulate metal
    return new THREE.MeshLambertMaterial(m);
}

function Head() {
    let head = new THREE.Mesh(Ball(g_robot.head.r, 60, 160), createMaterial({ color: g_color }));
    return head;
}

function Body() {
    let body = new THREE.Mesh(Cylinder(g_robot.body.r, g_robot.body.r, g_robot.body.h, 8, 1), createMaterial({ color: g_color }));
    return body;
}

function Shoulder() {
    let shoulder = new THREE.Mesh(HalfBall(g_robot.shoulder.r, 32, 32), createMaterial({ color: g_color }));
    return shoulder;
}

function Arm() {
    let leg = new THREE.Mesh(Cylinder(g_robot.arm.r, g_robot.arm.r, g_robot.arm.h, 8, 1), createMaterial({ color: g_color }));
    return leg;
}

function Hand() {
    let hand = new THREE.Mesh(Ball(g_robot.hand.r, 32, 32), createMaterial({ color: g_color }));
    return hand;
}

function Leg() {
    let leg = new THREE.Mesh(Cylinder(g_robot.leg.r, g_robot.leg.r, g_robot.leg.h, 8, 1), createMaterial({ color: g_color }));
    return leg;
}

function Foot() {
    let foot = new THREE.Mesh(HalfBall(g_robot.foot.r, 32, 32), createMaterial({ color: g_color }));
    return foot;
}

function Light() {
    const color = 0xffffff;
    const intensity = 1;
    const light = new THREE.DirectionalLight(color, intensity);
    light.position.set(-50, 40, 200);
    // var spotLight = new THREE.SpotLight(0xffffff);
    // spotLight.position.set(3000, 4000, 3500);
    // spotLight.shadow.camera.near = 2;// 投影近点
    // spotLight.shadow.camera.far = 8000;// 投影远点
    // spotLight.shadow.camera.fov = 5000;// 视场有多大
    // spotLight.lookAt(0, 0, 0);// 望向
    // spotLight.castShadow = true; // 允许投射阴影
    // spotLight.shadow.mapSize.width = 2048;	// 阴影贴图宽度设置为2048像素
    // spotLight.shadow.mapSize.height = 2048;	// 阴影贴图高度设置为2048像素
    // spotLight.shadowCameraVisible = true;// 开启调试模式
    // jscene.add(spotLight);
    return light;
}

function Robot() {
    const head = Head();
    head.position.y = g_robot.body.h / 2 + g_robot.head.r;

    const body = Body();

    const shoulderL = Shoulder();
    shoulderL.position.y = g_robot.body.h / 2 - g_robot.shoulder.r / 2;
    shoulderL.position.x = g_robot.body.r + g_robot.shoulder.r;
    const shoulderR = Shoulder();
    shoulderR.position.y = g_robot.body.h / 2 - g_robot.shoulder.r / 2;
    shoulderR.position.x = -(g_robot.body.r + g_robot.shoulder.r);

    const armL = Arm();
    armL.position.x = shoulderL.position.x;
    armL.position.y = shoulderL.position.y - g_robot.arm.h / 2;
    const armR = Arm();
    armR.position.x = shoulderR.position.x;
    armR.position.y = shoulderR.position.y - g_robot.arm.h / 2;

    const handL = Hand();
    handL.position.x = armL.position.x;
    handL.position.y = armL.position.y - g_robot.arm.h / 2 - g_robot.hand.r;
    const handR = Hand();
    handR.position.x = armR.position.x;
    handR.position.y = armR.position.y - g_robot.arm.h / 2 - g_robot.hand.r;

    const legL = Leg();
    legL.position.y = -g_robot.body.h / 2 - g_robot.leg.h / 2;
    legL.position.x = -g_robot.body.r / 2;
    const legR = Leg();
    legR.position.y = -g_robot.body.h / 2 - g_robot.leg.h / 2;
    legR.position.x = g_robot.body.r / 2;

    const footL = Foot();
    footL.position.y = legL.position.y - g_robot.leg.h / 2 - g_robot.foot.r;
    footL.position.x = legL.position.x;
    const footR = Foot();
    footR.position.y = legR.position.y - g_robot.leg.h / 2 - g_robot.foot.r;
    footR.position.x = legR.position.x;

    const robot = new THREE.Group();
    robot.add(head);
    robot.add(body);
    robot.add(shoulderL);
    robot.add(shoulderR);
    robot.add(armL);
    robot.add(armR);
    robot.add(handL);
    robot.add(handR);
    robot.add(legL);
    robot.add(legR);
    robot.add(footL);
    robot.add(footR);

    return robot;
}

function main() {
    // position
    const canvas = document.querySelector('#demo');
    const renderer = new THREE.WebGLRenderer({ canvas, /*antialias: true,*/ alpha: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(innerWidth, innerHeight);
    // camera
    // const fov = 100;
    const frustumSize = 100;
    // const aspect = window.innerWidth / window.innerHeight;
    const aspect = canvas.clientWidth / canvas.clientHeight;
    const near = 0.1;
    const far = 400;
    console.log(aspect)

    // const camera = new THREE.PerspectiveCamera(fov, aspect, near, far)
    const camera =
        new THREE.OrthographicCamera(
            frustumSize * aspect / -2,
            frustumSize * aspect / 2,
            frustumSize / 2,
            frustumSize / -2,
            near,
            far);
    camera.position.z = 100;
    // scene
    const scene = new THREE.Scene();

    // let helper = new THREE.GridHelper(1000, 40, 0x303030, 0x303030);
    // helper.position.y = frustumSize / -2;
    // scene.add(helper);

    // light
    scene.add(Light());

    const robot = Robot();
    scene.add(robot);

    function render(time) {
        time *= 0.001;
        robot.rotation.x = time;
        robot.rotation.y = time;
        robot.rotation.z = time;
        renderer.render(scene, camera);
        requestAnimationFrame(render);
    }
    requestAnimationFrame(render);
}
main()