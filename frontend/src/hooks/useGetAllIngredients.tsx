import { useQuery } from '@tanstack/react-query'
import { useCallback } from 'react'
import { Configuration, IngredientsApi } from '../api/generated'
import { API_BASE_URL } from '../App'



export const useGetAllIngredients = () => {
    const config: Configuration = {
        basePath: API_BASE_URL,
        isJsonMime: () => {
            return true
        },
    }
    const ingredientAPI = new IngredientsApi(config)

    const getAllIngredients = useCallback(async () => {
        return ingredientAPI
            .getAllIngredientsGet()
            .then((response) => {
                return response.data
            })
            .catch((error) => {
                throw error
            })
    }, [])

    const { data: allIngredients, isLoading: isLoadingAllIngredients } =
        useQuery({ queryKey: ['allIngredients'], queryFn: getAllIngredients })

    return { allIngredients, isLoadingAllIngredients }
}
