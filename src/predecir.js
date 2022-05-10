import { useEffect, useState } from "react";
import Resultados from "./resultados";

function Predecir() {
  const [texto, setTexto] = useState("");
  const [clase, setClase] = useState("");
  const url = "https://back-museums-uniandes.herokuapp.com/api/museums";

  const handleSubmit = (event) => {
    console.log("Concepto del paciente: ", texto);
    fetch(url)
      .then((res) => res.json())
      .then((museums) => {
        console.log("Texto", texto);
        document.getElementById("resultado").innerText =
          "El paciente pertenece a la clase: " + texto;
        //setTexto(museums);
      });
    event.preventDefault();
  };

  const handleChange = (event) => {
    setTexto(event.target.value);
    event.preventDefault();
  };

  return (
    <div className="form-group">
      <form onSubmit={(event) => handleSubmit(event)}>
        <label>
          Concepto del paciente:
          <input
            type="text"
            value={texto}
            onChange={(event) => handleChange(event)}
          />
        </label>
        <input type="submit" />
      </form>

      <p id="resultado"></p>
    </div>
  );
}

export default Predecir;
