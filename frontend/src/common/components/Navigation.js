import React from 'react'
import {Link} from 'react-router-dom'
import styled from 'styled-components'

const Navigation = ()=>(<Nav>
<NavList>
    <NavtItem><Link to="/counter-old">counter</Link></NavtItem>
    <NavtItem><Link to="/sign-up">User Join</Link></NavtItem>
    <NavtItem><Link to="/todo">todo</Link></NavtItem>
    <NavtItem><Link to="/math">수학</Link></NavtItem>
    <NavtItem><Link to="/linear">선형</Link></NavtItem>
    <NavtItem><Link to="/nonlinear">비선형</Link></NavtItem>
    <NavtItem><Link to="/brute-force">Brute Force</Link></NavtItem>
    <NavtItem><Link to="/divide-conquer">Divide And Conquer</Link></NavtItem>
    <NavtItem><Link to="/greedy">Greedy</Link></NavtItem>
    <NavtItem><Link to="/dp">Dynamic Programming</Link></NavtItem>
    <NavtItem><Link to="/back-tracking">Back Tracking</Link></NavtItem>
</NavList>
</Nav>
)
export default Navigation

const Nav = styled.div`
    width:100%;
    height:30px;
    border-bottom: 1px solid #d1d8e4;
    `                                                                

const NavList = styled.ul`
    width:1080px;
    display: flex;
    margin: 0 auto;
`

const NavtItem = styled.li`
    width: 70px auto;
    margin-left: 18px;
    margin-top: 5px;
    display: flex;
`