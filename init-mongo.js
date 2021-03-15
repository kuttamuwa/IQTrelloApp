db.createUser(
    {
        user:"iquser",
        pwd:"figo1190",
        roles: [
            {
                role:"readWrite",
                db:"iqmongodb"
            }
        ]
    }
)