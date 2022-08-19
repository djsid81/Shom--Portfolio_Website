function convert() 
{

  let inputNumber = document.getElementById("input-number").value
  let metricToImperialLength = inputNumber * 3.281
  let metricToImperialMass = inputNumber * 2.205
  let metricToImperialVolume = inputNumber / 3.78541
  let ImperialToMetricLength = inputNumber / 3.281
  let ImperialToMetricVolume = inputNumber * 3.78541
  let ImperialToMetricMass = inputNumber / 2.205

  document.getElementById("convert-length").textContent = inputNumber + " meters = " + metricToImperialLength.toFixed(3) + " feet | " + inputNumber + " feet = " + ImperialToMetricLength.toFixed(3) + " meters";
    
  document.getElementById("convert-volume").textContent = inputNumber + " liters = " + metricToImperialVolume.toFixed(3) + " gallons | " + inputNumber + " gallons = " + ImperialToMetricVolume.toFixed(3) + " liters";

  document.getElementById("convert-mass").textContent =inputNumber + " kilos = " + metricToImperialMass.toFixed(3) + " pounds | " + inputNumber + " pounds = " + ImperialToMetricMass.toFixed(3) + " kilos";

}

