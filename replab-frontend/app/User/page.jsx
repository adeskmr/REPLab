import { getServerSession } from "next-auth";
import { options } from "../api/auth/[...nextauth]/options";
import React from "react";
import { redirect } from "next/navigation";

const User = async () => {
  const session = await getServerSession(options)

  if(!session){
    redirect("/api/auth/signin?callbackUrl=/User");
  }
  return (
    <div>
      <h1>User Session</h1>
      <p>{session?.user?.email}</p>
      <p>{session?.user?.role}</p>
      </div>
  )
}

export default User