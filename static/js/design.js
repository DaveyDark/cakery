import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const shapes = ["Circle", "Square", "Rectangle", "Heart"];
const icings = [
  "Roses",
  "Flowers",
  "FlowersFull",
  "Flakes",
  "FlakesFull",
  "Cubes",
];
const icingChoices = [
  "CircleRoses",
  "CircleFlowers",
  "CircleFlowersFull",
  "CircleFlakes",
  "CircleFlakesFull",
  "CircleCubes",
  "SquareRoses",
  "SquareFlowers",
  "SquareFlowersFull",
  "SquareFlakes",
  "SquareFlakesFull",
  "SquareCubes",
  "RectangleRoses",
  "RectangleFlowers",
  "RectangleFlowersFull",
  "RectangleFlakes",
  "RectangleFlakesFull",
  "RectangleCubes",
  "HeartRoses",
  "HeartFlowers",
  "HeartFlowersFull",
  "HeartFlakes",
  "HeartFlakesFull",
  "HeartCubes",
];

const loader = new GLTFLoader();

const renderer = new THREE.WebGLRenderer({
  canvas: document.querySelector("#three-container"),
});

const scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff); // 0xffffff is white in hexadecimal RGB
const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
const light = new THREE.AmbientLight(0xffffff, 2);
scene.add(light);
camera.position.z = 0.35;
camera.position.y = 0.35;
camera.rotateX(THREE.MathUtils.degToRad(90));
renderer.setSize(500, 500);
const controls = new OrbitControls(camera, renderer.domElement);

let model; // Variable to store the loaded model

loader.load("/static/cakes.glb", function (gltf) {
  model = gltf.scene;

  // Set all objects to be invisible by default
  model.traverse(function (object) {
    if (object.isMesh) {
      object.visible = false;
    }
  });

  scene.add(model);

  showObjectByName(document.getElementById("shapeSelect").value, shapes, model);
  changeObjectMaterial(
    document.getElementById("shapeSelect").value,
    document.getElementById("flavorSelect").value,
    model,
  );
  let icingChoices = icings.map(
    (i) => document.getElementById("shapeSelect").value + i,
  );
  const icing =
    document.getElementById("shapeSelect").value +
    document.getElementById("icingSelect").value;

  console.log(icing);
  console.log(icingChoices);

  showObjectByName(icing, icingChoices, model);
  changeObjectMaterial(
    document.getElementById("shapeSelect").value +
      document.getElementById("icingSelect").value,
    document.getElementById("icingFlavorSelect").value,
    model,
  );

  // Render scene
  animate();
});
function showObjectByName(objectName, objectNamesList, model) {
  objectNamesList.forEach((name) => {
    const object = model.getObjectByName(name);
    if (object) {
      object.visible = name === objectName;
    }
  });

  animate();
}
function changeObjectMaterial(objectName, materialName, model) {
  // Traverse through the model and find the object with the specified name
  model.getObjectByName(objectName).material =
    model.getObjectByName(materialName).material;

  // Render the scene to reflect the material change
  animate();
}

function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();

document.getElementById("shapeSelect").addEventListener("change", () => {
  showObjectByName(document.getElementById("shapeSelect").value, shapes, model);
  const icing =
    document.getElementById("shapeSelect").value +
    document.getElementById("icingSelect").value;

  showObjectByName(icing, icingChoices, model);

  changeObjectMaterial(
    document.getElementById("shapeSelect").value,
    document.getElementById("flavorSelect").value,
    model,
  );

  changeObjectMaterial(
    document.getElementById("shapeSelect").value +
      document.getElementById("icingSelect").value,
    document.getElementById("icingFlavorSelect").value,
    model,
  );
});
document.getElementById("flavorSelect").addEventListener("change", () => {
  changeObjectMaterial(
    document.getElementById("shapeSelect").value,
    document.getElementById("flavorSelect").value,
    model,
  );
});
document.getElementById("icingSelect").addEventListener("change", () => {
  const icing =
    document.getElementById("shapeSelect").value +
    document.getElementById("icingSelect").value;

  showObjectByName(icing, icingChoices, model);
});
document.getElementById("icingFlavorSelect").addEventListener("change", () => {
  changeObjectMaterial(
    document.getElementById("shapeSelect").value +
      document.getElementById("icingSelect").value,
    document.getElementById("icingFlavorSelect").value,
    model,
  );
});
