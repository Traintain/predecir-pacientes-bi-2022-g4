import { useEffect, useState } from "react";

function Resultados(props) {
  const [texto] = useState(props.input.text);
  const [clase] = useState("");

  const url = "https://back-museums-uniandes.herokuapp.com/api/museums";

  useEffect(() => {
    fetch(url)
      .then((res) => res.json())
      .then((museums) => {
        console.log("Museums", museums);
        console.log("Texto", texto);
        //setTexto(museums);
      });
  }, []);

  return (
    <div>
      <p>El paciente pertenece a la clase: {clase}</p>
    </div>
  );
}

export default Resultados;
