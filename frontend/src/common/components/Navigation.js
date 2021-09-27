import React from 'react'
import {Link} from 'react-router-dom'
import styled from 'styled-components'

const Navigation = ()=>(<Nav>
<NavList>
    <NavtItem><Link to="/counter">counter</Link></NavtItem>
    <NavtItem><Link to="/todo">todo</Link></NavtItem>
    <NavtItem><Link to="/math">수학</Link></NavtItem>
    <NavtItem><Link to="/linear">선형</Link></NavtItem>
    <NavtItem><Link to="/nonlinear">비선형</Link></NavtItem>
    <NavtItem><Link to="/bruteForce">Brute Force</Link></NavtItem>
    <NavtItem><Link to="/divideConquer">Divide And Conquer</Link></NavtItem>
    <NavtItem><Link to="/greedy">Greedy</Link></NavtItem>
    <NavtItem><Link to="/dynamicP">Dynamic Programming</Link></NavtItem>
    <NavtItem><Link to="/backTracking">Back Tracking</Link></NavtItem>
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