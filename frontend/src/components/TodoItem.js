import React from "react"

class TodoItem extends React.Component {
    render() {
        return <li>
            <input
                type="checkbox"
                checked={this.props.todo.checked}
                onChange={() => this.props.handleChangeProps(this.props.todo.id)}
            />
            <button onClick={() => this.props.deleteTodoProps(this.props.todo.id)}>
                Delete
            </button>
            {this.props.todo.title}

            {/*<input type="checkbox" checked={this.props.todo.completed}/> {this.props.todo.title}*/}
        </li>
    }
}

export default TodoItem


// import React from "react"
//
// function TodoItem(props) {
//   return <li>{props.todo.title}</li>
// }
//
// export default TodoItem