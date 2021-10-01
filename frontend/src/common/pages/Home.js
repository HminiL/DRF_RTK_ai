import { SignIn } from "common";
import React from "react";
import { connect } from "api";

export default function Home() {
    // connection 확인용도
    const handleClick = e => {
        e.preventDefault()
        alert('Home Click')
        connect()
        .then(res => { alert(`접속성공 : ${res.data.connection}`)})
        .catch(err => { alert(`접속실패 : ${err}` )})
    }
    return(<div>
        <button style={{margin:'0 auto'}} onClick={handleClick}>Connection</button>
        <SignIn/>
    </div>)
}