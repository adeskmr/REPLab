import GitHubProvider from "next-auth/providers/github"
import GoogleProvider from "next-auth/providers/google"
import AppleProvider from "next-auth/providers/apple"

export const options = {
    providers: [
        GitHubProvider({
            profile(profile) {
              console.log("Profile GitHub: ", profile);
      
              let userRole = "GitHub User";
              if (profile?.email == "jake@claritycoders.com") {
                userRole = "admin";
              }
      
              return {
                ...profile,
                role: userRole,
              };
            },
            clientId: process.env.GITHUB_ID,
            clientSecret: process.env.GITHUB_Secret,
        }),
        GoogleProvider({
            profile(profile) {
                console.log("Profile Google: ", profile);

                let userRole = "Google User";
                return {
                    ...profile,
                    id: profile.sub,
                    role: userRole,
                };
            },
            clientId: process.env.GOOGLE_ID,
            clientSecret: process.env.GOOGLE_Secret,
        }),
        // AppleProvider({
        //     profile(profile) {
        //         console.log("Profile Apple: ", profile)

        //         return {
        //             ...profile,
        //             id: profile.sub,
        //             role: userRole,
        //         };
        //     },
        //     clientId: process.env.APPLE_ID,
        //     clientSecret: process.env.APPLE_Secret,
        // }),
    ],
    callbacks: {
        async jwt({token, user}) {
            if (user) token.role = user.role;
            return token;
        },
        async session({session, token}){
            if(session?.user) session.user.role = token.role;    
            return session;
        }
    },
}