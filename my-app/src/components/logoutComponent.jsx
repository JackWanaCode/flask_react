import React, {Component} from 'react';
import axios from 'axios';


class LogoutComponent extends Component{

    logout_help() {
        const config = {
            headers: {Authorization: 'Bearer ' + sessionStorage.getItem('token')}
        }
        // console.log("this is headers", config)
        axios.post('http://localhost:5000/logout', {}, config)
            .then(() => {
                console.log("You log out succesful")
            }).catch(() => {
                console.log("Login failed")
            });
    }

    render(){
        const config = {
            headers: {Authorization: 'Bearer ' + sessionStorage.getItem('token')}
        }
        // console.log("this is headers", config)
        axios.post('http://localhost:5000/logout', {}, config)
            .then(() => {
                console.log("You log out succesful")
            }).catch(() => {
                console.log("Login failed")
            });
        return(
            <>
                <div>You are logged out</div>
            </>
        )
    }
}

export default LogoutComponent