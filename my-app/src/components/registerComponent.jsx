import React, {Component} from 'react';


class RegisterComponent extends Component{
    constructor(props) {
        super(props)
        this.state = {
            username: '',
            password: ''
        }
        this.handlerChange = this.handlerChange.bind(this)
        this.handlerClicked = this.handlerClicked.bind(this)
    }

    handlerChange(event){
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handlerClicked(){
        console.log(this.state.username, this.state.password)
    }

    render() {
        return(
            <>
                <h1>Register</h1>
                Username: <input type="text" name="username" value={this.state.username} onChange={this.handlerChange}/>
                Password: <input type="password" name="password" value={this.state.password} onChange={this.handlerChange}/>
                <button onClick={this.handlerClicked}>Submit</button>
            </>
        )
    }

}

export default RegisterComponent