import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")

# Create a reference to the Google post.
doc_ref = db.collection("posts").document("Google")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())

# This time, we're creating a NEW post reference for Apple
doc_ref = db.collection("posts").document("Apple")

# And then uploading some data to that reference
doc_ref.set({
	"title": "Apple",
	"url": "www.apple.com"
})
