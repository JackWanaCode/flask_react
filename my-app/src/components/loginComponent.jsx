import React, {Component} from 'react';
import axios from 'axios';


class LoginComponent extends Component {

    constructor(props) {
        super(props)
        this.state = {
            username: '',
            password: ''
        }
        this.handlerChange = this.handlerChange.bind(this);
        this.loginClick = this.loginClick.bind(this);
    }

    handlerChange(event) {
        // console.log([event.target.name], event.target.value)
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    loginClick() {
        // console.log(this.state.username, this.state.password)
        let data = {username: this.state.username, password: this.state.password}
        let headers = {'Content-Type': "application/json"}
        let json = JSON.stringify(data)
        axios.post('http://localhost:5000/login', json, {headers: headers})
            .then((res) => {
                console.log("You are login succesful")
                console.log(res.data.token)
                sessionStorage.setItem('username', this.state.username)
                sessionStorage.setItem('token', res.data.token)
            }).catch(() => {
                console.log("Login failed")
            });
    }

    render () {
        return (
            <div>
                <h1>Login</h1>
                Username: <input type="text" name="username" 
                value={this.state.username} onChange={this.handlerChange}/>
                Password: <input type="password" name="password" 
                value={this.state.password} onChange={this.handlerChange}/>
                <button onClick={this.loginClick}>Login</button>
            </div>
        )
    }
}

export default LoginComponent