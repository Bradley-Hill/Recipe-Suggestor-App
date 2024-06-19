export interface Recipe {
  _id: string
  name: string
  total_time: number
  image_url: string
  ingredients: string[]
  instructions: string[]
  users_added:string[]
}
