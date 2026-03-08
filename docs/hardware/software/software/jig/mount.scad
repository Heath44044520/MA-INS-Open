// Simple 3D-printed sensor mount for TPBR piezo + ESP32
$fn=60;
difference() {
  cube([120,80,30]);
  translate([10,10,5]) cube([100,60,30]); // piezo recess
}
echo("Print this and mount your TPBR stack inside");
