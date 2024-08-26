import { useQuery } from '@tanstack/react-query'
import { useCallback } from 'react'
import {
    Configuration,
    Recipe,
    RecipesApi,
    RecipeCategories,
} from '../api/generated'
import { API_BASE_URL } from '../App'




export const useGetAllRecipes = (category?: RecipeCategories) => {
    const config: Configuration = {
        basePath: API_BASE_URL,
        isJsonMime: () => {
            return true
        },
    }
    const recipeAPI = new RecipesApi(config)
    const getAllRecipes = useCallback(async (category?: RecipeCategories) => {
        return await recipeAPI
            .getAllRecipesGet(category)
            .then((response) => {
                return response.data
            })
            .catch((error) => {
                throw error
            })
    }, [])
    const { data: allRecipes, isLoading: isLoadingAllRecipes } = useQuery<
        Recipe[]
    >({
        queryKey: ['allRecipes', category],
        queryFn: () => getAllRecipes(category),
    })

    return { allRecipes, isLoadingAllRecipes }
}
