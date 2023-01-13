import React from "react"
import ReactDOM from "react-dom"

// const element = <h1>Hello from Create React App</h1>
// ReactDOM.render(element, document.getElementById("root"))

//component file
import TodoContainer from "./components/TodoContainer"

ReactDOM.render(
    <React.StrictMode>
        <TodoContainer/>
    </React.StrictMode>,
    document.getElementById("root"))