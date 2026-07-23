import type { z } from "zod";

const API_BASE_URL =
	process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export async function apiClient<TSchema extends z.ZodType>(
	path: string,
	schema: TSchema,
	options?: RequestInit,
): Promise<z.infer<TSchema>>;
export async function apiClient(
	path: string,
	schema: null,
	options?: RequestInit,
): Promise<void>;
export async function apiClient<TSchema extends z.ZodType>(
	path: string,
	schema: TSchema | null,
	options?: RequestInit,
): Promise<z.infer<TSchema> | undefined> {
	const response = await fetch(`${API_BASE_URL}${path}`, {
		headers: {
			"Content-Type": "application/json",
			...options?.headers,
		},
		...options,
	});

	if (!response.ok) {
		throw new Error(`API request failed: ${response.status}`);
	}

	if (response.status === 204) {
		return;
	}

	const data: unknown = await response.json();

	if (schema === null) {
		return;
	}

	return schema.parse(data);
}
