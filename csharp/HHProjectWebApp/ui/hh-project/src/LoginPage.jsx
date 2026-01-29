import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs"
import LoginCard from './components/LoginCard'
import RegisterCard from './components/RegisterCard'

let isSignIn

function setSignIn(value) {
    isSignIn = value
}
export {isSignIn, setSignIn}


function LoginPage() {

    const API_URL="https://localhost:7219/api/"
    const navigate = useNavigate()

    async function loginClick(e) {
        e.preventDefault()

        var Email=document.getElementById("email").value
        var Password=document.getElementById("password").value

        const data = {
            Email: Email,
            Password: Password, }
        console.log(data)

        const headers = new Headers()
        headers.set("Content-Type", "application/json")

        fetch(API_URL+"User/login",{
            method:"POST",
            headers: headers,
            body: JSON.stringify(data),
          }).then((result)=>{
            if(result.status == 200){
                setSignIn(true)
                navigate('/')
            } else 
                alert("Пользователь не зарегистрирован.")
          })

    }

    async function registerClick(e) {
      e.preventDefault()

      var Email=document.getElementById("newEmail").value
      var Password=document.getElementById("newPassword").value

      const data = {
          Email: Email,
          Password: Password, }
      console.log(data)

      const headers = new Headers()
      headers.set("Content-Type", "application/json")

      fetch(API_URL+"User/register",{
          method:"POST",
          headers: headers,
          body: JSON.stringify(data),
        }).then((result)=>{
          if(result.status == 200){
              setSignIn(true)
              navigate('/')
          } else 
              alert("Пользователь не зарегистрирован.")
        })

  }

  return (
    <div className=''>
      <Tabs defaultValue="account" className="w-[400px] mx-auto pt-20">
      <TabsList className="grid w-full grid-cols-2">
        <TabsTrigger value="account">Вход</TabsTrigger>
        <TabsTrigger value="password">Регистрация</TabsTrigger>
      </TabsList>
      <TabsContent value="account">
        <LoginCard loginClick={loginClick}/>
      </TabsContent>
      <TabsContent value="password">
        <RegisterCard registerClick={registerClick}/>
      </TabsContent>
    </Tabs>
    </div>
  )
}

export default LoginPage
