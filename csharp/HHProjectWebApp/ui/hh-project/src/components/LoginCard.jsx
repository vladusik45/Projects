import React from 'react'
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
import { Button } from './ui/button'

function LoginCard({loginClick}) {
  return (
    <div>
      <Card>
          <CardHeader>
            <CardTitle>Вход</CardTitle>
            <CardDescription>
              Только авторизованные пользователи могут добавлять вакансии и резюме.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-2">
            <div className="space-y-1">
              <Label htmlFor="name">Email <span className='text-red-500'>*</span></Label>
              <Input id="email" placeholder="Email" required={true}/>
            </div>
            <div className="space-y-1">
              <Label htmlFor="username">Пароль <span className='text-red-500'>*</span></Label>
              <Input id="password" type="password" placeholder="Пароль" required={true}/>
            </div>
          </CardContent>
          <CardFooter>
            <Button onClick={loginClick}>Войти</Button>
          </CardFooter>
        </Card>
    </div>
  )
}

export default LoginCard
