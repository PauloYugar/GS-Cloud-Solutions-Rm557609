variable "prefix" {
  description = "Prefixo para nomear os recursos"
  type        = string
}

variable "location" {
  description = "Região da Azure"
  type        = string
  default     = "brazilsouth"
}
