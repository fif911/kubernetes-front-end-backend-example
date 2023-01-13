import React, {Component} from "react"

class InputTodo extends Component {
    state = {
        title: "",
    };

    onChange = e => {
        // console.log("hello");

        this.setState({
            // title: e.target.value
            [e.target.name]: e.target.value
        });
    };

    handleSubmit = e => {
        e.preventDefault(); //  preventing the default behaviour of the form submission.
        console.log(this.state.title);
        this.props.addTodoProps(this.state.title, this.state.description);
        this.setState({
            title: "",
        });
    };

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input type="text" placeholder="Add todo..." value={this.state.title} name="title"
                       onChange={this.onChange}/>
                <button>Submit</button>
            </form>
        )
    }
}

export default InputTodo